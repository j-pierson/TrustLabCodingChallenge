# TrustLabCodingChallenge

My approach:

For my solution to this problem, I used the Common Crawl data from May through August of 2020
as I thought these months would have the most desirable information due to the economic impact
at those times.

I obtained 60 sections (20 from each period May/June, July, and August) from Common Crawl, which
are stored in the data.txt file, and then used a keyword bank to determine whether each url (1,293,364 in total)
matched the description of "pages from the common crawl archive that discuss or are
relevant to COVID-19’s economic impact."

My keywords were: pandemic, economy, buiness, jobs, covid, coronavirus

To get ideal url's I required that at least 4 of the keywords showed up on the page's plaintext
and that the total number of appearances of the keywords was greater than 10.

This program runs in around 20 minutes on my MacBook Pro and I believe the results are desirable.
Still, there is much that I would like to and know I could improve on given more time.
