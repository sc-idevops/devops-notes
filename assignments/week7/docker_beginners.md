#What is Docker?
##Containers
Docker manages containers which are portable packages of applications which contain everything you need to run it
###For Devs
The idea is developers dont have to install, configure, and maintain services required on their development environment. 
The containers have their own isolated OS environments
###For Deployment
Operations no longer has to worry about managing a bunch of objects (artifacts) and instruction sets from developers
No longer have to worry about dependency conflicts or configuration problems

##What Makes a Container?
* small linux base image
* application files
* configuration data
These are set up in layers identified by hashes. These are downloaded and assembled based on a "recipie"

#Images
These are actual image files that can be moved around
an image is a running container environment

##Comparison vs Virtual Machine
an OS has two layers, kernel and application.
docker images have only 1 layer to deal with and therefore are smaller and start faster than a traditional VM which needs to use both layers.
VMs can be run anywhere, whereas docker images cant


