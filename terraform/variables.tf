# Common variables
variable "project_id" {
  type        = string
  description = "The project ID to host the cluster in"
}
variable "region" {
  type        = string
  description = "The region to host the cluster in"
  default     = "europe-west2"
}
variable "env_name" {
  type        = string
  description = "The environment for the GKE cluster"
  default     = "dev"
}
variable "ip_range_pods" {
  type        = string
  description = "The secondary ip range to use for pods"
  default     = "ip-range-pods"
}
variable "ip_range_services" {
  type        = string
  description = "The secondary ip range to use for services"
  default     = "ip-range-services"
}

# VPC variables
variable "network" {
  type        = string
  description = "The VPC network created to host the cluster in"
  default     = "gke-network"
}
variable "subnetwork" {
  type        = string
  description = "The subnetwork created to host the cluster in"
  default     = "gke-subnet"
}

# GKE variables
variable "cluster_name" {
  type        = string
  description = "The name for the GKE cluster"
}
variable "zones" {
  type        = list(string)
  description = "The project ID to host the cluster in"
  default     = ["europe-west2-a", "europe-west2-b"]
}
variable "node_pool_name" {
  description = "Name of the node pool"
  type        = string
  default     = "node-pool"
}
variable "machine_type" {
  description = "Machine type for nodes"
  type        = string
  default     = "e2-small"
}
variable "node_locations" {
  description = "Comma-separated list of zones where nodes will be created"
  type        = string
  default     = "europe-west2-b,europe-west2-c"
}
variable "min_nodes" {
  description = "Minimum number of nodes in the node pool"
  type        = number
  default     = 2
}
variable "max_nodes" {
  description = "Maximum number of nodes in the node pool"
  type        = number
  default     = 5
}
variable "disk_size_gb" {
  description = "Disk size for nodes in GB"
  type        = number
  default     = 30
}
variable "service_account" {
  description = "Service account to associate with the node pool"
  type        = string
  default     = "service-account-name"
}
