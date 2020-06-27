---
layout: post
---

I haven't been in the industry very long, but the term "legacy code" has been
slowly infecting my vocabulary and I want to talk about it.

The term legacy usually implies archaic, old, back when the earth was flat and
we didn't have C++11 - it has a negative connotation (shoutout to my middle
school English teachers, only reason I know that word) and thus carries a
negative tone whenever engineers use it in a sentence. Even Google defines it
specifically within the "computing" category with a negative connotation.

> adjective [COMPUTING]
>
> denoting or relating to software or hardware that has been superseded but is
> difficult to replace because of its wide use.

This is frusturating to me though - legacy code is everywhere, it's reliable,
and we can learn from it. It's sent us to the damn moon and back, and on 2MHz.
We only want to change the legacy because we realized we didn't do it right the
first time; we want to add one more feature, fix one more bug, or implement one
optimization we scribbled down a while back. The problem isn't the code, it's
us.

![there's a picture here, I swear](/assets/apollo11_comparison.jpg)

Side note, Apollo 11 had [2048 _words_ of RAM and 36864 words
ROM](https://en.wikipedia.org/wiki/Apollo_Guidance_Computer). For reference you
would need at least 15000 Apollo 11 AGCs to spin up a JVM, depending on which
version you want. All for.. what? Basically a really strict scripting language
with horrible metaprogramming? I don't know what Margaret Hamilton is doing
right now but I wouldn't be surprised if she enjoyed writing Apollo 11 code more
than dealing with the black hole of volatile memory that sits behind modern
JVMs.

Anways, back to the rant. You don't like legacy code? Don't write it. I just
recently graduated from a world in which my assignments revolved around
timeboxed, limited-scope programming assignments that are no sooner forgotten
than throw in the garbage. It made sense to write code that just got the job
done - Git histories could be destroyed, tests were never handed back, and
university fileshares are overwritten. However in the real world (something that
professors notably forget to mention a lot about), you don't get a do-over
without someone with a different degree coming down and chatting with you.

Sometimes when thinking about legacy code I wander off into the depths of some
popular SVN or Git repository just to see how it all started. Did Chrome really
just start with "Hello world?", was Linus just as sassy back in the 90s as he is
now? Take [the original commits for
Chromium](https://github.com/chromium/chromium/commits/master?after=893d2bf2d93235c2dfba55b9b3dc4dfe673e612a+904570).
Doesn't look like much eh? Well that's because they had no idea the code they
wrote would be run on the computers of [64%](https://gs.statcounter.com/) of all
people that use the internet. Now their code is forever preserved in the history
of Chrome. If they knew they were writing legacy code, wouldn't they have
written [better
code](https://github.com/chromium/chromium/commit/b98cb228710ec0afcd2f0470fc43140772c8c0c9)?

I've gone on too long. My point: as long as you're writing code for someone
else, it's legacy code. Write good code. Take your time. Use polymorphism
sparingly. Design once. Pick tabs or spaces and don't switch. Pick a style guide
and don't change. If you don't, the legacy code you wrote yesterday suddenly
becomes the problem you're solving today, instead of more important things -
like how we're getting to the moon.
