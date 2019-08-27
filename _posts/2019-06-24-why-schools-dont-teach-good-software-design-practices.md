---
layout: post
title: "Why Schools Don't Teach Good Software Design Practices"
categories: programming
---

The short answer is that good software design **should** be taught, but unfortunately is lost amid the large swath of topics in the curriculum. However, these sort of questions are hardly ever black and white, so let's dive a little deeper.

# Nobody's code makes sense but yours
If you've ever worked on a group project (which I assume almost everyone has), then you've definitely run into issues with your group members at some point. Whether it's not doing their work on time, turning in crappy work, or not being cooperative, the end result is that the team is less efficient and your stress level has finally caused you to snap.

Working with other people's code is similar, and possibly even more frustrating. The major pain point is that you're not working with just your team's code, but also code that was written by third-party developers and those no longer part of the team. If they wrote something that looks like gibberish and left no documentation to guide users, a lot of resources will be wasted on deciphering the code.

At this point, you're furious, you've torpedoed your computer with your fist, and claim that nobody's code makes sense but yours.

# Syntax vs. Design
There's a distinct difference I have to make before talking about software design. Syntax is the arrangement of commands/words in a programming language whereas design is defining a structure in which components of your code live. This is an important distinction because while both syntax and design contribute to code complexity, how you make them “good” is very different.

Good syntax, once defined, is easily enforced. For example, style checkers are automated scripts that run in the background of your development environment and inform you when to indent lines, break up long lines of code, and fix syntax errors. Design on the other hand, is good when a user or developer easily understands your project structure. Code is properly separated, modules accomplish a well defined task, and the files are relatively easy to navigate.

Although implementation details are important, **higher level abstractions provide clarity and focus into what you’re doing**.

# 5 Reasons Good Software Design Isn't Taught
With that in mind, it makes you wonder why good design is largely ignored. Here are some of the main reasons:

## 1. It's not the focus of the curriculum
Our schools tend to focus on implementing data structures, analyzing algorithms, and building things that work rather than building things that last. After having interacted with many of my peers and talking with industry professionals, it’s obvious there’s a gap when it comes to design.

One reason for this gap is ironically a direct result of having researchers teach courses. A researcher will prioritize their research (obviously) over good design, which is perfectly acceptable. Unfortunately, this is often also reflected in any projects that students are assigned. The focus is the topic students are learning, not their design.

But when design is not the focus, you can end up with terribly written code. The example below is an example of one such piece:

```python
etld = read_file(“some file”)

...

def parse_qsr(tld):
	tmp = ''
	ld = ['www', 'blog', 'example', 'com']
	for level in ld:
		if level == 0:
			tmp += some_variable[len(var) - level – 1]
		else:
			...

def start():
	output = parse_qsr(tld=etld)
	...

start()
```

This is only a rough excerpt, but there are 3 main issues I want to point out:

1. `tmp += some_variable[len(var) – level – 1]` is simply getting the last element in the last. Simply do `tmp += some_variable[-1]`. This makes it much more readable.
2. The distance from where `etld` was defined and where it was used (it was several hundred lines of code in the actual file), makes it difficult to tell what’s going on. In addition, `etld` shouldn’t be a global variable if it’s only being used in one place.
3. The variable names made it very difficult to tell what they represented and the researcher did not leave any meaningful comments

While code doesn’t have to be perfect, several improvements could be made to make this excerpt more readable. 

## 2. Technology is developing faster than education systems can keep up with
With the major advances in technology in the past decade, some schools simply have trouble keeping up. Programming languages, development frameworks, and new organizational strategies are being developed at a rapid pace causing many schools to either fall behind or focus on less volatile topics. With so many tools being built, it’s understandable.

For example, [Github](github.com) was founded in 2008 and is now the largest open source web-hosting service for [version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control). To many, it is indispensable. The rise of techniques/tools such as [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development), [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing), and [Github](github.com) are just a few examples of technology contributing to this already complex landscape.

The result is that many professors simply don’t have enough exposure to these new tools. Whereas industry is required to keep up with best practices, professors do not. Unfortunately, this also means that students will also not be exposed to these tools, forcing many students to either pick it up on their own time or develop bad programming habits.

## 3. Project based learning ignores good software design practices

![xkcd_bad_code](/assets/posts/xkcd_bad_code.png)
*Comic by [xkcd](https://xkcd.com/) about bad code*

I briefly mentioned this in my first point, but **class projects ignore good design because they are not meant to last**. Since the work you’re doing is self contained and likely small in size, code quality and design are an afterthought. Your primary goal is to get something working, and even if a class does ask you to take into account design, it doesn’t go very in depth as to what makes good design. There’s usually a lack of time and resources for a professor to give quality, in-depth critiques on project design, resulting in gilded projects – operational on the outside, but unmaintainable inside.

Hackathons are the epitome of poor software design. For those unfamiliar, a hackathon is a programming sprint-like event in which teams of students work on a software project within an allotted time (usually anywhere from 12-36 hours). Most projects that are built within that time frame will have extremely poor code quality. Why? **Everyone wants to built something that works**. The teams need something to demo to the judges and students that walk around and many teams also want to win prizes. But that’s the exact mindset that would not work on any longer lasting project. You might tell yourself that once in a while, it’s okay, but at some point it becomes a bad habit, and when it does, it’ll be too late once you’re working on a large project.

## 4. Good and bad design can be subjective
Good design can be subjective, and while that isn’t necessarily bad, it certainty makes it harder to teach. At the surface level, everybody can agree that breaking large chunks of code into manageable modules or classes makes sense, but what if you had hundreds of these classes that had all sorts of dependencies with each other. What is the optimal solution to organize these classes so that someone unfamiliar with the code can quickly understand what’s going on?

One thing you could do is attempt to group together related classes. What defines code as related then? What happens if there’s a few classes that seem to depend on a lot of other classes? Do you break the classes into folders? Separate them into [Docker](https://en.wikipedia.org/wiki/Docker_(software)) containers? Maybe put them in completely separate repositories? The questions go on forever, but a decision needs to be made. Nonetheless, good design needs to be emphasized more so that students can begin to question whether what they have is logical.

## 5. Bureaucracy and other misc. barriers
Sometimes, it really is just bureaucracy getting in the way. Adding a new core requirement requires all sorts of paperwork I don’t fully understand, but I understand enough to know that it’s an arduous process. And when focusing on good design isn’t a priority (see #1), it’s easily lost in the mountain of issues an educational institution needs to handle.

# Stepping up your code game
If you’re a developer or simply want to learn more about good design, I’ve compiled a short list of resources I thought were pretty good. Just like most people, I’m still working on improving my design skills and so I wanted to share some things I’ve looked at before.

## Short list of resources
- [Mythical Man Month](https://www.cs.drexel.edu/~yfcai/CS451/RequiredReadings/MythicalManMonth.pdf): This book contains many nuggets of wisdom about managing large software design projects that are sometimes counter-intuitive
- [Quora - What are the characteristics of a good design in software engineering?](https://www.quora.com/What-are-the-characteristics-of-a-good-design-in-software-engineering): A nice TLDR of things to consider when designing systems. If you read the responses you’ll see that there isn’t a single unified answer
- [Fundamental Principles of Good System Design](https://www.researchgate.net/publication/276087136_Fundamental_Principles_of_Good_System_Design): A research article covering good design techniques in a more formal manner than the rest of the resources I’ve linked to
- [System Design Cheatsheet](https://gist.github.com/vasanthk/485d1c25737e8e72759f): A good, albeit very technical, list of things to consider when designing highly scalable systems

# Fun Fact
Ironically enough, many talented researchers write messy code (bad design and syntax!). Just google [PhD's with bad code](http://bfy.tw/OCjT) and you'll see what I mean.
