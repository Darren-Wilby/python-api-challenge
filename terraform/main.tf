# Gather authentication details for Google Cloud Platform
data "google_client_config" "default" {}

# Define the Kubernetes provider configuration with the GKE cluster endpoint and access token
provider "kubernetes" {
  host                   = "https://${module.gke.endpoint}"
  token                  = data.google_client_config.default.access_token # Access token for authentication
  cluster_ca_certificate = base64decode(module.gke.ca_certificate)        # Cluster CA certificate for secure communication
}

# Create the GKE cluster using the Terraform module
module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  version                    = "26.1.1"
  project_id                 = var.project_id
  name                       = "${var.cluster_name}-${var.env_name}"
  regional                   = true
  region                     = var.region
  zones                      = var.zones
  network                    = module.gcp-network.network_name
  subnetwork                 = module.gcp-network.subnets_names[0]
  ip_range_pods              = var.ip_range_pods
  ip_range_services          = var.ip_range_services
  http_load_balancing        = false
  network_policy             = false
  horizontal_pod_autoscaling = false
  filestore_csi_driver       = false
  create_service_account     = true
  logging_service            = "logging.googleapis.com/kubernetes" # Logging service to use for the cluster

  # Configuration for the node pool(s) within the cluster
  node_pools = [
    {
      name            = var.node_pool_name
      machine_type    = var.machine_type
      node_locations  = var.node_locations
      min_count       = var.min_nodes
      max_count       = var.max_nodes
      disk_size_gb    = var.disk_size_gb
      spot            = false
      auto_upgrade    = true
      auto_repair     = true
      autoscaling     = true
      service_account = "${var.service_account}@${var.project_id}.iam.gserviceaccount.com"
    },
  ]

  # OAuth scopes define the permissions granted to nodes in the node pools
  node_pools_oauth_scopes = {
    all = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
      "https://www.googleapis.com/auth/trace.append",
      "https://www.googleapis.com/auth/service.management.readonly",
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/servicecontrol",
    ]
  }

  node_pools_labels = {
    all = {}

    default-node-pool = {
      default-node-pool = true
    }
  }

  node_pools_metadata = {
    all = {}
    node-pool = {
      # Custom script to gracefully drain nodes during maintenance operations
      shutdown-script                 = "kubectl --kubeconfig=/var/lib/kubelet/kubeconfig drain --force=true --ignore-daemonsets=true --delete-local-data \"$HOSTNAME\""
      node-pool-metadata-custom-value = "node-pool"
    }
  }

  # Taints allow nodes to repel certain pods based on their attributes
  node_pools_taints = {
    all = []

    node-pool = [
      {
        key    = "node-pool"
        value  = true
        effect = "PREFER_NO_SCHEDULE"
      },
    ]
  }

  node_pools_tags = {
    all = []
    node-pool = [
      "node-pool",
    ]
  }
  depends_on = [
    module.gcp-network
  ]
}