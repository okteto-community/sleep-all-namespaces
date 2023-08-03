# Sleep all your Okteto namespaces on a schedule

> This is an experiment and Okteto does not officially support it. 

1. Create an Okteto token (user must be admin)
1. Create the following secrets on your Okteto instance.

        SLEEP_OKTETO_URL=https://okteto.example.com
        SLEEP_OKTETO_TOKEN=XXXXXX
        SLEEP_JOB_SCHEDULE="0 20 * * *"
1. Create a namespace, and, via the admin section, mark it as 'keep awake'. 
1. Update the schedule on okteto.yaml if needed.
1. Run `okteto deploy -n $NAMESPACE` to build the image and create the cronjob.

