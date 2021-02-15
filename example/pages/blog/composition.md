title: Configuration, Composition, Customization
byline: How to reason about program structure and make better estimates for change.
tags: Coding, Architecture, Technical
published: 2021-10-1

Imagine you're trying to solve a tech problem. You're getting paid $50,000 to solve it, no matter how long it takes you.

Good news! There's a piece of open-source software that solves it... Mostly. Probably if you tweak the settings it will work. All you have to do is **configure** it. Ace!

Bad news! After a day of tweaking, you find that actually it doesn't solve your problem. You need one more feature. You're going to have to **customize** it. Unfortunately it's a big, monolithic piece of software, with terrible documentation, and this might take you a long, long time with massive refactors.

Now if the software was made well, it might have a **composition** layer. Then the software is a bunch of pieces that work together, and you can change how these pieces work. If that was the case, you might just have to refactor one piece of it, and/or how you put it together. Wouldn't that be awesome.

## The Three C's

So we've got three levels here:

### Configuration

Tweak settings that are defined by the program to alter how it works. Often well documented, these tend to be single values, rarely defining relations. This feels very powerful, like the system is asking you questions, and you're just telling it what to do. Examples: Application settings, command-line options, json, ini, and yaml files.

### Composition

Define relations, hierarchy, and configure components within the system. It feels like you are bringing pieces together like lego. It can feel more like design work than engineering. Examples: HTML, CSS, XML, Unix pipelines, no-code systems. Often a composition layer is actually in the code as a high level api or collection of inheritable types and mixins.

### Customization

Change directly the logic of how the program or components of it work. This tends to get into direct compiled or interpreted languages. This feels very programmery, like you're putting that education to work. It feels like we're executing on our purpose. JavaScript, Python, C, etc.

## The Problem

As programmers, we love the idea of lego. The concept of composition is something many of us really strive toward. We call it "modular". But it's so hard to get there for a few reasons.

The first is emotional. Between feeling powerful, feeling like we're executing on our purpose, and feeling like we're designers... Which two do you think developers strive for. Not the latter, that's for sure.

The second is we tend to think either up or down, configuration or customization, but not towards the middle. It's easy to imagine many ways that a user might want to alter how the program works, and for each way we can offer a setting.

## The Benefit

Now that you are thinking it terms of configuration, composition, and customization this helps us estimate
