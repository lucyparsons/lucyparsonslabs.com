---
layout: post
title: "Data Release: Mapping Search Warrants in Chicago"
image: images/blogimages/search-warrants.png
author: lucyparsonslabs and matt_chapman
teaser: "The Chicago Police Department executed an average of six search warrants per day. Here's what we know:"
tags:
  - Chicago
  - data
  - FOIA
---

The Chicago Police Department executed an average of six search warrants per
day over a five year period. Approximately 40% of those did not lead to an
arrest. A data analysis by Lucy Parsons Labs shows a startling lack of control
in executing warrants by the police department with troubling human rights
implications.

In 2019, CBS News has reported that Chicago police [have pointed guns at
children](https://chicago.cbslocal.com/2019/05/04/key-body-camera-footage-missing-after-chicago-police-officers-raid-wrong-homes-point-guns-at-children/)
and routinely [raid the wrong
locations](https://chicago.cbslocal.com/2019/07/19/wrong-raids-chicago-police-krystal-archie-family-federal-lawsuit/),
sometimes multiple times. Given the high number of search warrants executed a
day, this data raises questions about how much latitude judges are giving when
cops describe the "persons, houses and effects" they want to search.

Today’s data release, [available on
GitHub](https://github.com/lucyparsons/cpdsearchwarrants), is the result of
multiple Freedom of Information Act (FOIA) requests sent by Lucy Parsons Labs
over the past year. CPD [initially
replied](https://www.muckrock.com/foi/chicago-169/search-warrant-log-56379/) to
us that they maintain no responsive records when we requested this data.

Critically absent from this data are unexecuted search warrants. Chicago police
claim they do not track these warrants.

![](/images/blogimages/search-warrants.png)

Our analysis found that from 2012 to 2017, over 45 percent of all executed
search warrants did not result in any arrests. In one neighborhood, North
Lawndale, three of the four warrants executed saw no arrest.

The search warrants clustered in predominantly Black and poor neighborhoods,
repeating similar patterns found in our [asset forfeiture
investigation](/posts/HitsThePoor/) and [stop and frisk data
set](/posts/stop-and-frisk/).

As noted today’s
[article](https://reason.com/2019/07/23/chicago-police-executed-more-than-11000-search-warrants-in-mostly-poor-neighborhoods-over-5-year-period/)
at *Reason.com*, "a lack of an accompanying arrest is not necessarily an
indicator of a botched raid. For example, the police may obtain warrants to
search phones and other electronics". The requirement to obtain a warrant to
search a cell phone follows the _Riley v California_ Supreme Court decision.

Working alongside FOIA expert and data scientist Matt Chapman, Lucy Parsons Labs
is also providing a data visualization tool, allowing the public to analyze the
data. It can be [viewed online](https://viz.mchap.io/search_warrants) and
includes census-tract level of detail. In a statement, Chapman said:  

> Our hope with this app is that it helps others understand the deep seeded dynamics
> of inequality across Chicago even just a little bit more. We have submitted a series
> of FOIA requests for significantly more search warrant information. Once Chicago
> gives us the records from those requests, we'll be able to add more to the application
> and making it that much more useful.

The application lets viewers analyze the activities of the police in their
neighborhood by filtering the data by specific wards in Chicago. Feedback and
suggestions are welcome at `info @ lucyparsonslabs DOT com`.

This data helps deepen the public's understanding of the criminal system in
keeping with the mission of the [Chicago Data
Collaborative](https://chicagodatacollaborative.org/), of which LPL is a member.
