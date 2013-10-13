LOUDBIRD
========

What is it?
-----------

A Python script that reads tweets aloud.

Wait... What?
-------------

Using whatever local voice synthesis you have available it will read the
tweets from whatever sources you provide. It keeps track of what's been
read and will read new tweets since last time run. The idea is that you
could fire this off from a cron job (or whatever local crap your OS
provides) and it runs periodically to check for new tweets.

Erm... why in the world would you want that?
--------------------------------------------

Well, I don't know why *you* would want that (freak), but personally I find
shit like FloridaMan pretty funny and yet can't bring myself to constantly
recheck twitter every few minutes to get a chuckle. What I *really* want
is someone to read it to me, and since Nick Offerman isn't available, I
wrote this instead.

Okay, so how do I use it?
-------------------------

### Configuration ###

First, you need to configure it. You can either make the config file by
hand, or run it with 'genconf' to generate a default config, or just run
it and watch it fail (it will generate a config as well). The preferred
way is 'genconf':

       ./loudbird.pu genconf

If a config file is already there when genconf is run, it will be backed
up.

The config file has two sections:

#### [twatter] ####

This section is the general configuration of the Twitter interface and
the underlying speech synthesizer. Your app and oath keys go in the
appropriate key settings. The 'rate adjust' setting is used to slow
down or speed up the rate of speaking.

#### [following] ####

This is where you list the Twitter accounts to follow, The format is
one account per line, with either the ID on the right of the equal sign
or a negative number to indicate how many to go back from the top most
tweet.

So, if I was following FloridaMan and criswell (me), and I wanted to
have loudbird start at the 10 most recent tweets for each, my following
section would look like:

       [following]
       _FloridaMan = -10
       criswell = -10

### Running ###

Once you're configured, simply run loudbird.py. It can bde run manually,
and/or run from cron (or whatever).

       ./loudbird.py

Loudbird will automatically update .loudbird.conf with the most recently
read tweets for each user. This means you really shouldn't update the
'following' section manually any more (unless you wish to reset it). So
in our example above, after running a few times it might start looking
like this:

       [following]
       _FloridaMan = 38171627181
       criswell =  8384741111

Each subsequent run of loudbird will only read those tweets that are new
since the last run. If no new tweets can be found, it will not read them.


