## Tell me about yourself
My name is Kevin, I graduated with a Master's in Computer Science at TCD and I love building projects and solving problems.
I have experience as an intern at Arista Networks where I worked on the backend of their flagship product, CloudVision,
where I gained experience in Python and Golang, as well as tools such as git, linux, and google workspace.
I also enjoy building other layers of the stack,
I have built frontend and full stack projects in college and personally, using technologies such as Node.js,
TypeScript, Flask, React, Next.js, MongoDB, and SQL. I believe my experience and my passion would make me a great
fit to the company.

## Tell me about a project you worked on
Sure, for my dissertation I worked on a smart window notification system, which is basically a system that sends a
notification to the user on an app to open or close the window based on the indoor air quality. The purpose of the
project was to see how effective the use of a notification system based on environmental data from sensors
is at influencing air quality in an enclosed environment.
- Talk about the microcontroller with sensor I built using an ESP32 and gyroscope sensor and sends data to MQTT broker
- Talk about web framework (with REST API and MQTT) built with Flask that gets sensor data from Smart Citizen API
- Talk about mobile app built with Flutter
- Used simple feed forward neural network to determine open or close window
- Temperature, humidity, TVOC (Total Volatile Organic Compounds), eCO2, PM2.5 (inhalable particulate matter with diameter
<= 2.5 microns), PM1, PM10

## What was a typical day like at your internship?

A typical day would be working on tasks assigned to me, whether it's working on a new feature or fixing bugs.
I'd push my changes, wait for the CI/CD pipeline to run tests, and if something breaks I would debug it.
I would then wait for someone to review my code, which usually would be my mentor.
We would have meetings throughout the day. There would be weekly meetings for a specific package or feature.
We mainly used google meet and chat for meetings and collaboration. I would use it to ask questions and get help from
other engineers.

## What was the biggest thing you learned during your internship?

Honestly, it was writing production-quality code. In college, if your code works you're mostly done,
but at Arista, you had to format and style your code correctly in order to make the linter happy,
you had to cover all edge cases, write tests, and have it perform well. I also learned to get better at reading
other people's code and working in a large codebase, which is completely different from starting projects from scratch.

## What are you most proud of from your internship?

Seeing my connectivity monitor script getting used and making a difference. It felt great to see my code running in
production and actually helping other people do their jobs better. I also came in not knowing any Golang, and by
the end of it I was adding features and fixing bugs to a core product API, which felt like a big accomplishment.

## Tell me about a time you were in a difficult situation and how you handled it.

So during my internship at Arista, I was working on the Connectivity Monitor Action Script. The initial approach seemed
solid, basically I'd compare the current connectivity stats to previous stats, calculate the percentage difference, and 
if it exceeded a threshold, the action would fail and roll back the changes. I implemented it, then ran it on a test
cluster, and at first it seemed fine, but then I'd realise that it would fail and roll back changes
that were completely fine. It turns out, there were random spikes in connectivity stats like latency and jitter even
when the connectivity were normal.
This was difficult as I had already spent a whole week on this and now had to go back to the drawing board and figure
out a different implementation. I was stuck on what to do, so I ended up reaching out to my mentor, and we tried to
figure out another solution. We ended up having a meeting about this with our manager, and it was then CUSUM was brought
up, which was a statistical approach that would detect anomalies over time. Instead of comparing just two data points,
I'd use the connectivity monitor API to gather historical data, calculate the mean and std, and then use CUSUM
to see how much current stats were deviating from the baseline.
It took some time to implement but in the end it was working very well, it went through proper testing by the
testing team. The script was then shipped to production.

## Tell me about a time you failed at work, and what did you learn from it?

- Similar to above answer
So during my internship at Arista, I was working on the Connectivity Monitor Action Script. I had designed and
implemented the initial approach, which was to compare the current connectivity stats to previous stats, 
calculate the percentage difference, and  if it exceeded a threshold, the action would fail and roll back the changes.
I tested it locally, it seemed to work, and I felt pretty confident about it. I pushed it for review and my mentor
approved it, so we started testing it in more realistic scenarios.
That's when things fell apart.
- Turns out there were random spikes...
- The failure wasn't just the approach didn't work, it was that I didn't test it thoroughly before committing to it.

## What's an area of weakness you're working on/what's your biggest weakness?

I'd say one of my biggest weaknesses is I tend to be late asking for help. I usually try to solve things myself
and spend hours or even a couple of days before I finally reach out for help. I think what I realised is that
there can be tight deadlines and not reaching out for help for a long time can be bad. So what I think I'll try and do
is give myself a time limit then ask for help, which will help me be more productive.

## Why do you want to work for this company?

I want to work for (company) because I like the idea of being able to work on AI applications that get used by
real businesses, which I find exciting. When I did my internship, it was really satisfying seeing my work go into
production and being used by real clients. Another reason is the culture around integrity, I really like the fact that
(company) really emphasises about doing the right thing and speaking up when something doesn't feel right, which really
matters to me. And the opportunity as well, being able to work in a big company like (company), and working at the
(location), which I actually visited when I went to that _ Meetup organised by (name), it seemed like a nice
building.
