NAME ?= danisan

all: ps-me im-me

im-me:
        docker images | grep ${NAME}

ps-me:
        docker ps -a | grep ${NAME} 

#notes:
#the name is a variable
#the command will use all the docker containers with the name either in the image name or the container name
#read the docs has a username, not usre if we can use the name of the app as well.
