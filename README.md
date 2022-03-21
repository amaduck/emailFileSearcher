# emailFileSearcher
Searches .eml files for phrases

Standard functionality for most email clients allows you to search your inbox for a particular phrase. Lotus Notes does not allow this, or at least my version of Notes doesn't. This program will run through email files looking for particular phrases from a particular sender, and return a list of emails that match the criteria.

To use:
1) Place email files to be checked in the emails subfolder
2) Edit the sender details and phraselist you're checking for. 
3) Phrase list can contain one or more words. NB: per issue below, that words can be split over two lines in Notes .eml files, so using multiple single words may work where using a long phrase doesn't

# Issues
1) Notes seems to enforce a line length (of 73 chars in files I've looked at), and will split words across lines, with an equals sign. Eg me could become m=
e (where "m=" is the end of one line, and "e" is the beginning of the next). This program won't register that instance of "me". I suspect it would be possible to resolve this with more work on the email parser, but I've found the email I wanted, and this is a pretty niche use case

# Potential Improvements
1) Prompt for email sender and phrases, rather than hardcoding
2) Make better use of parser to check words as they appear in html, rather than checking underlying code

I was looking for a particular email, and found it using this - don't envisage doing much more work on this
