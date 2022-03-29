wordpress will have a pod and a svc of a load balancer. they operate on a database

environment variables must match up with what's expected by the program.
consult with the dockerhub file for the technology:

when connecting an application to a database you need 4 values:
    * database name
    * host name
    * database_username
    * password
    
helm is a package manager for kubnernetes. we can use it to set up mysql for us.

it spits out a lot of stuff for us to handle, including getting the root password of the database.

Now we need to securely store this information in our deployment.
there is a section type in the yaml template called secrets.
reference others on how to use them

next comes productionizing things:
 * putting env vars into secrets
 * ingress controllers
 * ssl cert for custom domain
