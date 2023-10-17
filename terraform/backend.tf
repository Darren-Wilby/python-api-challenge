terraform {
  backend "gcs" {
    bucket = "darrens-gke-terraform-tfstate-bucket-01" # GCS bucket name to store terraform tfstate
    prefix = "react-flask-cluster"                     # Update to desired prefix name. Prefix name should be unique for each Terraform project having same remote state bucket.
  }
}