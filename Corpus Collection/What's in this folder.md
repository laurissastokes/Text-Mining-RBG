**SCDB_query_screenrecording**
---
A screenrecording demonstrating the query I performed in the Washington University Law Supreme Court Database (SCDB) to identify cases for which RBG wrote an opinion. 

**SCDBquerycasenames.csv**
---
A list of the names of the 458 cases that appeared in my SCDB query. I scraped these from the SCDB query search results pages using a free Google Chrome browser plugin. 

**texts_uncleaned_courtlistener.tar.gz**
---
Contains the html that I retrieved through the courtlistener links provided through my SCDB query. I scraped the links using a free Google Chrome browser plug in. Then I used a free command line utility called wget to automatically download them all. I changed the extension from html.mth to .txt, but other than that, these texts are entirely uncleaned versions.

**texts_uncleaned_findlaw.tar.gz**
---
95 of the courtlistener links were redirecting. So, for those cases, I went back and did the same thing, seeking the findlaw links instead. I changed the extension from html.mth to .txt, but other than that, these texts are entirely uncleaned versions.

**texts_uncleaned_justia.tar.gz**
---
The SCDB doesn't include Supreme Court opinions beyond the 2018 term. So, for the more recent opinions, I went to https://www.oyez.org/cases/2019 (which links to justia) and manually downloaded the ones that contained an opinion authored by RBG. I changed the extension from html.mth to .txt, but other than that, these texts are entirely uncleaned versions.

**courtlistener_casenames.csv**
---
A list of the names of cases that I downloaded from the courtlistener links. I scraped the cases names  from all the courtlistener cases using the script called **titles.py** 

**findlaw_casenames.csv**
---
A list of the names of the cases that I downloaded from the findlaw links. I scraped these using a free application called OpenRefine.

**justia.casenames.csv**
---
A list of names of the cases that I downloaded from the justia links. I scraped these using a free application called OpenRefine.
