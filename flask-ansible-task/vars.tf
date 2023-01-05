variable "app_name" {
  type = string
    default = "scard-ansible-task"
}

variable "port" {
  type = number
    default = 80
}

variable "subnets" {
  type = list
    default = ["subnet-0357bbe188bd1e4c8", "subnet-03ec22f87490c8dda"]
}

variable "availabilityZones" {
  type = string
    default = "us-west-2a"
}

variable "hcstatuscode" {
  type = string
    default = "200"
}

variable "hostedZone" {
  type = string
    default = "Z370FY5A2PDAE"
}