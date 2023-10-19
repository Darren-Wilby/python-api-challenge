# Module for creating a Google Cloud Platform (GCP) network with subnets and secondary IP ranges
module "gcp-network" {
  source       = "terraform-google-modules/network/google"
  version      = "6.0.0"
  project_id   = var.project_id
  network_name = "${var.network}-${var.env_name}"

  # Configuration for the primary subnet within the network
  subnets = [
    {
      subnet_name   = "${var.subnetwork}-${var.env_name}"
      subnet_ip     = "10.10.0.0/16"
      subnet_region = var.region
    },
  ]

  # Configuration for secondary IP ranges within the primary subnet
  secondary_ranges = {
    "${var.subnetwork}-${var.env_name}" = [
      {
        range_name    = var.ip_range_pods
        ip_cidr_range = "10.20.0.0/16"
      },
      {
        range_name    = var.ip_range_services
        ip_cidr_range = "10.30.0.0/16"
      },
    ]
  }
}