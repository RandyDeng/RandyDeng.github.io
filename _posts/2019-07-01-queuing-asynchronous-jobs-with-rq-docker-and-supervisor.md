---
layout: post
title: "Queuing Asynchronous Jobs with RQ, Docker, and Supervisor"
categories: programming
---

# RQ, Docker, Supervisor
In this tutorial, I'll be going over how to set up asynchronous jobs with RQ and Supervisor running inside Docker containers. It will cover everything including what each of these services are, why they were chosen, and the configuration files needed to setup our environment.

While reading this tutorial, you should go ahead and clone the code from [https://github.com/RandyDeng/rq-docker-supervisor](https://github.com/RandyDeng/rq-docker-supervisor). If you know what you're doing or want to jump right in, the repository has very simple instructions on getting started.

If you're unfamiliar with these services, keep reading and I'll explain them to you!

## Intro to Task Queues
When building an application, you'll often find that you need to run a lot of tasks (e.g. retrieving data, triggering analysis, handling API requests). These tasks can get triggered by users, sometimes in parallel, and you'll suddenly find yourself wondering how to handle these tasks efficiently.

This is where queuing systems come in. Queuing systems provide a framework that allow you to submit these tasks as jobs, which are then executed by workers. The workers all run independently, meaning the jobs are completed asynchronously, resulting in faster and cleaner processing. When complete, the results can be retrieved through the job. This process is shown in the diagram below:

![queue_system](/assets/posts/queue_system.png)

*Diagram of how a simple queuing system works*

## RQ
The great thing about queuing systems is that you don't have to create them from scratch. There's a multitude of frameworks available that all do similar things to varying degrees of complexity. A pretty good list of components of these systems can be found at [https://taskqueues.com](https://taskqueues.com).

For our purposes though, we will be using [RQ](https://python-rq.org/). RQ is a Python library for queuing jobs and processing them in the background with workers. It uses Redis as its database and was chosen because of its simplicity and ease of use.

In addition to RQ, we will also be using [RQ dashboard](https://github.com/eoranged/rq-dashboard). This will allow us to see everything about our system including jobs in the queues, worker details, and any errors that occur.

![queue_system](/assets/posts/rq_dashboard.png)

*An example RQ dashboard web page showing queue information*

If you cloned the repository, you'll notice that all of the components needed to create your system are already implemented! As you might have guessed, the `rq-dashboard` folder is what handles the dashboard creation. In the `workers` folder, you'll see `settings.py` and `supervisord.conf`. `settings.py` tells the workers which database and queues to connect to and `supervisord.conf` is a supervisor configuration file (see supervisor section).

Lastly, `docker-compose.yml` (which I'll explain shortly) is what will start up RQ dashboard, redis, and the RQ workers.

## Docker
[Docker](https://www.docker.com/) is a tool that allows operating-system-level virtualization to encapsulate and isolate different services. These environments are called containers, and docker is well-known for providing excellent containerization tools.

In this project we create 3 Docker containers: rq-dashboard, redis, and workers. Since these tasks serve very different purposes and their work is independent of each other, putting them in Docker containers allows us to isolate their environment. This allows us to easily modify, ship, deploy, or copy the container to a variety of different platforms.

[Docker Compose](https://docs.docker.com/compose/) is simply a tool that allows easy management of multiple Docker containers. Instead of running a bunch of terminal commands or defining several Dockerfiles, it makes much more sense to have a single file manage several containers at once. In addition, if you still have a need for a Dockerfile, Docker Compose allows you to run a Dockerfile with its Docker Compose configuration. If you look in `docker-compose.yml`, you will see the 3 Docker containers I mentioned above.

Since Docker can get very complex (Docker tutorials alone would take up several blog posts!), I will refer you to the [Docker documentation](https://docs.docker.com/) for specifics. There's also a lot of good resources online if you get stuck on something with Docker. To get started though, all you have to understand is that we have 3 containers and that these containers are created using the Docker Compose file and Dockerfiles.

## Supervisor
[Supervisor](https://python-rq.org/patterns/supervisor/) is a service that allows control of a number of processes on UNIX-like operating systems. Since our system will have more than one worker to allow more tasks to run asynchronously, it makes sense that we need some way to create all of them. Supervisor will allow us to do this by spawning multiple workers as individual processes.

The `supervisord.conf` file in the `workers` folder defines configuration details such as number of workers, process name, the command to run, and other miscellaneous settings. To update these values, simply change them in the file and restart your containers!

It is worth noting that supervisor is not necessary to work with RQ. You could have just as easily used [systemd](https://python-rq.org/patterns/systemd/) or some other process managing tool to accomplish the same thing. You could even write your own script if you felt like it! The point is that whatever you use, it should spin up the workers automatically once the worker container is created.

## Let's Finally Run It!
Now that you know how everything works, let's get it running. Keep in mind that supervisor will only work on UNIX-like machines! To work on Windows, you will need to find another solution.

The first step is to install Docker and Docker Compose. Follow the instruction in the following links:

- Install [docker CE](https://docs.docker.com/v17.09/engine/installation/)
- Install [docker-compose](https://docs.docker.com/compose/install/)

After installing that, simply run

`docker-compose build`

`docker-compose up`

That's it! Run `docker ps` to see the 3 containers you just created.

You can verify everything is working by visiting `localhost:9181`. You should see the dashboard and 5 workers.