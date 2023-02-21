
![Logo](https://github.com/AleCo3lho/zabbix-over-k8s/blob/dd07baaccd7a42552cf95174f704476640762d4d/image/zabbix-over-k8s.png)


# Zabbix on K8s

I built this repository to provide a quick and easy way to run Zabbix on K8s.

To get started, simply start Minikube on your machine and apply the file contained in the deploy folder.

If you want to use it in a cloud environment such as AWS or Azure, you need to change the class of the PVCs and also remove the storage class manifest since you will be using the storage class of your cloud.

I also stored some Python scripts that make it easier to import a list of URLs if you have many to upload.

Finally, there is a template with Web monitoring configured to make it easier to monitor your URLs.

You need to first import the template, then get the templateid and put it in the script that adds the URLs. You also need to put the hostgroupid of the group you want to add the URLs to.

If you have any questions, I am available to help.




## Authors

- [@AleCo3lho](https://github.com/AleCo3lho)

