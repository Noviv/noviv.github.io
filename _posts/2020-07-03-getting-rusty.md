---
layout: post
---

It's been a while since I've touched an open source project, let alone
contributed. So here's my attempt at taking a small bite - contributing to the
Rust language compiler. Probably starting with a timeline then my complaints
because I'm listening to bbno$ and it's about 1am in Seattle.

* [23:50] Playlist started.
* [00:25] `git clone https://github.com/rust-lang/rust.git`
* [00:41] 49%... it's taking a while to clone, 122k commits :O

Reading over the Rust language docs is actually a really pleasant experience -
having read (never participated) in [ugly LKML
threads](https://lkml.org/lkml/2013/7/13/132) and [particularly unfriendly
project entry points](https://gcc.gnu.org/git/gcc.git), I'm happy to see a
systems lang compiler that actually has a UX.

* [00:52] Got it all, time to `x.py`
* [01:01] Turns out I only have Python 3 in WSL, so I'm using `python3 x.py
build` - I really don't like Python as a build system.
* [01:19] Looks like this will take a while, probably a good time to sleep - I
also just saw that my social icons aren't showing up. Gotta remind myself to
fix this in [#1](https://github.com/Noviv/noviv.github.io/issues/1).
* [01:35] Psych, I stayed up; turns out I didn't install `cmake`. A quick `apt
install` and we're back on track. Gnight.
* [09:29] Gmornin. Build finished and it looks like it didn't take that long -
maybe 30 mins? Should have recoreded the time. `rustc --version` = `1.46.0-dev`
here we go!
* [09:47] Discovered a broken link in Rust's README! Time to make the world's
smallest PR.
* [09:52] I'm an _IDIOT_, I completely forgot to fork.
* [10:10] Fixed the fork, changed my remote URL, and created [this
PR](https://github.com/rust-lang/rust/pull/74003) to address my documentation
woes.
* [10:23] Turns out it was a duplicate - time to find something more useful to
contribute.
* [13:47] Got some new Salesforce hardware - time to set it up and have lunch.
I'll pick this up at a later time hopefully.
