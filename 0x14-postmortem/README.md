##Postmortem - web_stack_debugging

###Issue Summary
At 2:02AM PST on Thursday 03-30-17 a server dropped itself from the system due
to hardware failure and was immediately detected, diagnosed and replaced.
Users attempting to access their accounts (although none reported) would have
been denied. The server was down for a total of 45 minutes
(2:02AM PST 03-30-17 to 2:47AM PST 03-30-17) and potentially effecting 2,354
users. The down server was replaced within 30 minutes and back online within
15 minutes.

###Timeline
- 1:50 AM PST - Engineer noticed files missing during a routine check
- 2:02 AM PST - Server crashes while engineer inspected file system for file
manipulation
- 2:11 AM PST - Server is pulled from the rack and replaced
- 2:32 AM PST - Replacement server downloads from server slave
- 2:40 AM PST - Download complete and system reboot
- 2:47 AM PST - Server went back online and all accounts restored

###Root Cause and Resolution
While running routine diagnostics around 1:50 AM PST, an engineer attempted to
reboot Nginx web server which resulted in repeated failure. Upon closer
inspection, it was found that the file system was compromised. The main
configuration file was determined to be missing along with other key file
booting files. The engineer the queried the command history and found no
evidence of system configuration manipulation. Shortly after, the system
crashed (2:02 AM PST). After further inspection the cause was determined to
be a hard drive failure. The engineer immediately pulled the crashed server
after two failed reboot attempts and replaced it with a backup server
(2:11 AM PST). Once the server was replaced and booted, our engineer began
the backup protocol, downloading all content from the dedicated server slave
to the new server (2:32 AM PST). After a full diagnostic, the server was back
online and the accounts effected were fully restored with no user notice
logged (2:47 AM PST).

###Corrective and Preventative Measures
The failed server was due to be replaced within the following month with no
prior service interruption, it showed no reason for concern. Since this
is the second failed server incident within the past 2 months, it is decided
that server life expectancy will be cut from 5 years to 4 years with an
increase graded maintenance model(increase maintenance as server ages). Team
and Backups all performed as expected. Additional server side monitoring
measures will be put in place by 04-04-17 specifically aimed at performance
checking.
