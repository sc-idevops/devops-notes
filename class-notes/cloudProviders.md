# Cloud Providers

All cloud providers are doing one thing: a UI to provision compute services.
*compute services*: CPU/RAM/Storage/Network resources you can rent/consume
see also: platform or software or infrastructure as a service. (PaS/SaS/IaS)
RDS: Databases as a service

## AWS

AWS is compute services for rent from amazon.

EC2 Contains most of the primary services used on AWS:
- Instances
- Images
- Elastic Block Store
- Network & Security
- Load Balancing
- Auto Scaling

### EC2 Specifications

EC2: (Elastic Compute) is the **virtual machine** services AWS offers. A single VM is called an "instance"
AMI: Virtual Machine **Images** used by AWS. You can build these with packer. These are similar to what we use in docker.
  Note: Amazon's Linux Distro is based on CentOS. (Redhat)
EC2 Images have different "sizes"
- T instances are general purpose instances
- A types are for ARM architecture
- C are optimized for compute workloads (i.e. lots of CPU)
- R are memory optimized (i.e. lots of RAM needed)
- P are accelerated computing instances that have co-processors for some advanced math.

Logins can be protected with a *key-pair* (RSA or ED25519)
    W: This cannot be changed after you create it!

Network settings: *VPC* = virtual private network.
- Subnet: a subset of IPs assigned to this VPN.
  - see also: cidr subnet charts. /18 is the typical max allowed. (65,000+ IP addresses)
- Auto Assign Public IP: do you want this publically accessible from the internet?
- Security Group: IP firewall settings. typically only ssh is allowed.
  - anything else must be explicitly defined by you! this is the most common issue with connection issues in AWS.
  - example: allowing port 80 for nginix webserver.
  - custom types can be assigned to a specific CIDR group.
  - 0.0.0.0/0 = everywhere

Storage: how much space you need? There are different types:
- GP3 is the best SSD drives
- provisioned IOPS (input/output per second) can specify a threshhold of speed needed.
- Cold Storage: HDDs offering cheaper storage for files needed infrequently, like long term backups.

### AWS Services (These fall under EC2)

- Spot instance: a compute resource (instance) rented for an unknown time for a low price.
- Availability Zones: AWS has multiple datacenters all over the world.
  - in each region there's multiple availability zones. These zones are usually physically separated, in case of power/internet failure. You can't see other regions resources.
  - AWS Region affects the price!
- IAM Role: Permissions in AWS
- Lifecycle Management: removal of old snapshots, etc.
- When snapshotting, ensure you check the "no reboot" option.
- IP Addresses: 
  - Public IPs are not static and can change upon rebooting.
  - Elastic IPs are static ip address that can be assigned to compute resources to remedy this problem.
- Auto Scaling Groups: compute resources in these grow with your needs. additional instances are launched based on a set of rules.
  - Launch Templates indicate these rules. Min/Max numbers, availability zones, etc.
- Load Balancers: these balance network traffic between multiple backend points. round robin is the typical approach (iterate through list)

#### Route 53

- AWS's Hosted DNS server. DNS as a Service!
- dig command = DNS lookup

#### RDS

Amazon's Database as a service. Available in multiple types.
- Aurora DB
- Postgress
- MYSQL
- MSSQL
- MariaDB
Amazon's Aurora is MySQL but 30% faster
These also need security groups, network/subnets, etc. Connection issues? Start here!

snapshot = backup for AWS things
AWS actions can take a long time to process.

#### SQS - Simple Queue Service

Amazon's Message Queue System.
You queue an action on a website for consistent data. This is why your facebook post might not show up immediately.
No system on the planet can process millions of requests a second, so this system creates events that are later processed by your system.
These "messages" are typically JSON payloads that get processed.

#### SES - Simple Email Service

AWS email as a service.
This can be used to send large volumes of outbound email, like those promotional messages we all hate.

#### ECS & EKS - Elastic Container Service and Elastic Kubernetes Service

Docker & Kubernetes in AWS!
These docker-like images run server-less (anywhere)
Elastic Container Registry is like AWS's Dockerhub

EKS manages all the kubernetes stuff, you just specify what nodes to run what.

#### Lambda

Server-less running of applications. E.g. a java application that runs only when invoked (based on events)
*server-less in this sense means that you don't specify anything about what system it's running on, it's some computer somewhere doing the work*

#### AWS Storage

S3: Storage! You can put anything here. Its literally cloud storage.
- Key value storage into things called buckets
- S3 Glacier is used for infrequently accessed data at a lower price

finally something we don't have to worry about security groups (but you can set access controls)

#### Elasti-cache

Redis on AWS (in memory caching service)
Caching things in memory so things go faster!
Services Offered:
- Redis
- memcached
Session Data (logins) are often put in cache. This allows any instance to authenticate a user without them needing to log in to each instance.

like everything else these also use security groups etc.

#### DynamoDB

flat DB helpful for locking access to files like a terraform DB.

#### Amazon Cloudfront

Amazon's version of cloudfront, a Content Delivery Network.
Your website will be distributed and accessible from multiple locations. "serverless"

#### Amazon Cloudwatch

AWS's attempt at monitoring resources. Alerts can be set up for various criteria. 
Biggest Limitation is no agents run automatically on machines

There are better tools out there though:
- New Relic
- Data Dog
- Instana (for Kubernetes)
- Prometheus
- Graphana

#### AWS CloudTrail

Track user activity and API usage.
(Grant tracked the IP address of whoever hacked his AWS using this and the access logs.)

### AWS Security

IAM Permissions are not fun. They can be set for anything.

## Azure Cloud Services
