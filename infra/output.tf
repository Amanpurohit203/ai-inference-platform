output "cluster_name" {
  value = module.eks.cluster_name
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "ecr_repository_url" {
  value = "697015998406.dkr.ecr.ap-south-1.amazonaws.com/ml-inference-app"
}

output "vpc_id" {
  value = module.vpc.vpc_id
}