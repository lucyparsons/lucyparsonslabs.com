---
layout: page
title: "The State of IMSI Catching Catching"
#
# Content
#
author: freddy_martinez
teaser: "Recently, the Lucy Parsons Labs was sent an email about detecting IMSI catchers, often called Stingrays, at protests. Our experience detecting IMSI catchers in the last year is below."
categories:
  - stingray
tags:
  - technology
  - surveillance
#
# Styling
#
header: no
image:
 thumb: "thumbs/StingrayThumb.jpg"
---

This is an area with which I have a good bit of experience. I have spoken about Stingrays at conferences including [DEF CON](https://www.youtube.com/embed/JyTb5mJOYL) and [THOTCON](https://github.com/freddymartinez9/securitytalks/tree/master/Thotcon) and wrote a [guide for protests.](https://github.com/freddymartinez9/securitytalks/blob/master/IMSICatchersForActivists.md) The Lucy Parsons Labs has spent over a year seeking evidence of IMSI Catcher use at Chicago-area demonstrations. 

While our research has returned interesting data, over the last year we have found no confirmed hits of catchers in use at protests in Chicago. Our methodology faces critical technical limitations in both hardware and software, described below. (Note: In this blog post, the quoted text is from the email we received that sought our help.)

> There's a strong feeling in the activist communities around the country there is some sort of cell phone surveillance going on during protests, that is possibly being used to monitor/disrupt communication and identify protest leaders, but no one has yet been able to prove it in a solid manner.

The Lucy Parsons Labs' work has not captured a confirmed IMSI catcher being used in _Chicago-area_ protests, but there is significant evidence that Law Enforcement Officials (LEOs) are using IMSI catchers to surveil activists at demonstrations elsewhere in the county. For example, there is at least one purchase order for a Stingray in [Florida in 2004](http://www.documentcloud.org/documents/2169898-miami-dade-police-stingray-purchase-to-target.html) before the large-scale FTAA/anti-capitalism protests. Photographic evidence exists for a deployment in Dresden Germany and a deployment during unrest at [Taksim Square](https://gitlab.com/Hounge/Android-IMSI-Catcher-Detector) in Istanbul, Turkey. ([picture](http://i43.tinypic.com/2i9i0kk.jpg)) 

![Dresden](/images/blogimages/DresdenIMSICatcher.jpg)

There also seems to be evidence of a fake tower emerging in Kiev, where, [as the New York Times reported](http://thelede.blogs.nytimes.com//2014/01/22/ominous-text-message-sent-to-protesters-in-kiev-sends-chills-around-the-internet/), ominous text messages were sent to demonstrators (pictured below). This could have easily been done with an IMSI Catcher, which, as an added benefit of capturing phone numbers, could allow government agencies to send SMS messages to suspected protesters for free. 

![Kiev](/images/blogimages/Kiev.jpg)

It is, however, unclear how often this form of surveillance is happening in a protest context. (IMSI catchers are widely used otherwise in the United States for criminal investigations, often without meaningful oversight). While LEO use of an IMSI catcher would not make it possible to identify individual protest leaders, the practice would nonetheless allow governments a window into the social networks among protesters, an associational mapping that is both constitutionally fraught and a valuable commodity. 

Therefore, IMSI catcher use at protest is a realistic risk that one should incorporate into their threat model. 

> We have explored several avenues of getting this done, but have not found a way that we believe will reliably detect an attack by an IMSI-catcher device, and that will also generate some sort of report that we can use as proof.

Our efforts to unmask an IMSI catcher by technical means have taken several avenues, none of which has yet been able to both reliably detect an attack by an IMSI catcher device and also generate some sort of report that could serve as sufficient proof. The best evidence I have analyzed to date of a "capture" is the packet captures (pcaps) that LPL reviewed in [collaboration with NorthStar Post](http://nstarpost.com/17486/159855/a/cellphone-surveillance-used-on-black-lives-matter-protesters-at-fourth-precinct). The pcaps can be download directly at [this link](https://s3.amazonaws.com/nstarpost-public/imsicatcher-minn/snoopsnitch_2015-11-25_21-39-25UTC.pcap). Here, there is a request for an IMSI rebroadcast; this data, however, is not itself proof of an IMSI Catcher. Data points that might provide additional evidence for an IMSI Catcher include:

 * a new LAC appearing at / around the same time as the IMSI request. 
 * a new CID broadcasting or an empty CID that didn't exist before the IMSI request.
 * broadcasting on new ARFCN
 * long delays in ACK messags from the BTS 

With a given pcap, you would then do a calculation of all the network metrics and ascribe a score to how suspicious particular events are. (This methodology is in fact what SnoopSnitch does; we will talk about that below.)  In the case of the NorthStar Post pcaps, my analysis came out to medium probability. To me, it wasn't proof positive, although it is possible this data was in fact generated by an IMSI catcher.

There are several options for capturing information. There is Cryptophone, a fancy name for a modified Samsung Galaxy S3 which has a buggy baseband that allows direct access to it. Because a Cryptophone has direct access to the most interesting levels of the baseband OS, which is where the information we are interested in resides, it is a potential tool for countersurveillance. It is, however, expensive, and while I have seen their product a few times, it doesn't strike me accessible to most people for the price point. 

In addition to a stand-alone hardware solution, there are two software solutions, "SnoopSnitch" and "AIMSICD", both of which work on Android phones. SnoopSnitch requires root on your phone, which is needed since you need baseband access and is essential for IMSI Catcher detection. 

> If you were in our shoes, and attempting to catch IMSI-Catcher activity at a protests, what would you use?

The Lucy Parsons Labs, and our team of volunteers, run rooted Moto Es with SnoopSnitch. Once we have captured data, we can export pcaps off SnoopSnitch for further analysis into WireShark using their GSM filters. We have run the Moto Es with SnoopSnitch for over a year and have gotten no hits at protests. It surely a bit frustrating, but its unrealistic to pull out one phone at one protest and expect a hit. Most surprisingly is when we _didn't_ get hits, namely when POTUS was in town and near us -- we expected a hit given reports that he travels with an [IMSI Catcher](https://twitter.com/csoghoian/status/613110943514374146) and likely an IMSI Catcher Catcher. A likely reason for this absence is that, based on our review of SnoopSnitch, the software seems to be lacking support for 4G/LTE (something the team behind SnoopSnitch is working on). This form of countersurveillance is thus a work-in-progress; our methodology is always undergoing further development.

That doesn't mean I don't recommend running the SnoopSnitch on rooted Moto Es. Our best guess right now is to do a lot of reconnaissance and counter surveillance, which is time consuming because it must be done before and during demonstrations. We do need more individuals, and technical minded people running SnoopSnitch all over demonstrations, however I think it is important to be rigorous in your methodology and be reasonable with expectations.

See you at the RNC.
