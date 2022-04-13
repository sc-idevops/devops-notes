# Site Reliability Engineering (SRE)

Seen as a possible offshoot of DevOps, a lot of these practices involve keeping things:
* Reliable
* Available
* Scaleable
   
## Avoiding Technical Debt:
When deploying software so quickly you can pile up more malfunctions.
Finding ways to help test and avoid these things helps.

How can we create patterns in design and deployment to minimize technical debt?

## Monitoring Systems (Infrastructure & Applications)
Metrics:
* How long have processes been running?
* How many resources have these processes been using?

## Incident Response:
Understanding what happened (root cause analysis) and post mortems (wow morbid)
* Testing Items
* Bug Fixes
* Release Procedures

By planning things out, we can avoid problems before they happen

Change Management: Identifying when bugs happen in code

## Monitoring Tools
Application Performance Monitoring: Intrusive Detailed Monitoring of processes running on your machines.

User Monitoring: Collecting information on what our users are doing and what their experience is like.

Error Budgets: If you go over this, you're fired (jk)

---------------

# Homework:

What tools can we deploy on our Kubernetes cluster to know how everything is performing?
What metrics should we track? (here's an easy one, number of restarts)

# SRE TOOLS

## Monitoring Tools

- New Relic
- Data Dog
- Instana
- Prometheus/Grafana
- Dynatrace
- AWS Cloudwatch
- Azure Monitoring
- Elasticsearch/Kibana APM
- Elasticsearch/Kibana Anomaly Detection

## Types of Testing:
- Unit Testing
- Functional Testing
- Regression Testing
- User Experience Testing
- Chaos Testing
    - The act of introducing chaos to your infrastructure to see how fault tolerant it is. (Turn off random things, kill pods, etc)
    - Create chaos within an environment to see how a highly availale infrastructure will respond. (See also: Chaos Monkey)
        - Note: Not many companies are actually able to do this, it's more of an ideal state to be in.
- Load/Performance Testing

## On Call, Scheduling, & Alerting Tools
- Ops Genie
- VictorOps
- Pager Duty

