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
  Dashboard which shows overall health of not just your apps but can monitor your entire software stack.  
  As well as showing charts monitoring response times, it can show an index score of how closely your app is meeting your expected performance benchmarks.
  A thoughtput chart shows how much under load our infrastructure is.
  Slowest Transactions, Error Rates, etc. And a list of all the hosts your app runs on.

- Data Dog
  Another infrastructure monitoring Dashboard. They have 120+ preconfigured integrations with apps/services along with an API.
  Can run on cloud/bare metal/VMs/containers. Open source technology, can review the agent on github. (looks like python)
  the dashboards look exceptionally customizable and flexible. they can also be shared publically to your customers.
  most information is filtered by tags. automated alerts can be sent to relevant people based on criteria.
  collaboration and notetaking appears built in. 

- Instana
- Prometheus/Grafana
  service that queries apps to get specified metrics.
  Designed to help you ascertain how many users you have, sort through errors, response time. is it working?
  how are apps behaving? server results, database status. 
  out of box integration with programming languages and frameworks. 

- Dynatrace
  combines AI with performance monitoring to give you more details and answers about your applications. it is open with an API and SDK to extend its abilities via plugins. 

- AWS Cloudwatch
 designed for and provided by amazon for their services, which limits its scope compared to these other tools.  
- Azure Monitoring
- Elasticsearch/Kibana APM
  compared to centralized solutions like the ones above, elasticsearch collects metrics from different agents and combines it together for you to view instead of having to make existing code work with your chosen monitoring solution.
- Elasticsearch/Kibana Anomaly Detection
  automatically displays anomalies in your metrics for analysis.

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
these tools are more for alerting ops crew about problems when they happen so they can get working on fixing them. they provide timely detailed information to the correct people and can serve as a point of contact between technicians.

- Ops Genie
- VictorOps -> Splunk On-Call
  
- Pager Duty

