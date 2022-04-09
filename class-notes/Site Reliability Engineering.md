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

---------------

## Monitoring Tools
Application Performance Monitoring: Intrusive Detailed Monitoring of processes running on your machines.

User Monitoring: Collecting information on what our users are doing and what their experience is like.

Error Budgets: If you go over this, you're fired (jk)

# Homework:

What tools can we deploy on our Kubernetes cluster to know how everything is performing?
What metrics should we track? (here's an easy one, number of restarts)

