==============================
Fedora 20 Gnome edition review
==============================

:date: 2014-11-07 20:00
:tags: Fedora, Gnome Shell
:category: Linux
:slug: fedora-20-gnome-edition-review
:authors: Daniel Jonsson
:summary: Review of Fedora 20's Gnome Shell edition.

Where I am coming from
++++++++++++++++++++++

Before ending up at Fedora I have used multiple different Linux distributions,
a couple of which I will comment below on their up- and downsides from my
perspective.

Arch Linux
----------

The most recent Linux distribution I ran before installing Fedora on my desktop
was Arch Linux with KDE's Plasma Desktop. However, that only lasted for about a
month for various reasons.

To start with, I can not stand the installation process of Arch Linux and it
almost kept me up at night. If I ever wanted to reinstall the computer I would
need to wade through their installation guide once again and spend hours to set
the computer up. I obviously managed to install it, and it went quite smoothly
if I am going to be honest, but needing a manual for installing an operating
system and hours of my time feel unacceptable.

My second gripe with Arch Linux is all those small problems I encountered
throughout the system. For instance, Samba shares did not appear in Dolphin,
Firefox did not render the fonts on one WordPress blog I maintain, OwnCloud's
KWallet password management was a pain to set up and I experienced problems
when I installed Wine. I am sure that there were more problems that I have
managed to suppressed by now. My belief is that these problems are the result
of the rolling nature of Arch and the lack of a polished and curated experience
from the distribution's developers and maintainers.

The crown though of Arch Linux is the `Arch User Repository
<https://wiki.archlinux.org/index.php/AUR>`_ (AUR) where all packages of your
imagination can be found, easily accessible. It gets even easier to install
AUR packages when you have installed a third-party wrapper of Arch's package
manager Pacman, for example `Yaourt
<https://wiki.archlinux.org/index.php/Yaourt>`_.  However, I once experienced
problems installing a package from the AUR, so I asked about it on Arch's
discussion board and immediately received flack for using a wrapper of Pacman,
which I find strange since the AUR is an official part of Arch Linux and it is
one of the main reasons for running Arch.

Ubuntu
------

Ubuntu was the first Linux distribution I used, and I have used it on and off
since about 2005. But there is often something that bugs me and forces me to
either reinstall it or try something else.

I really like the looks and functionality of Ubuntu's default desktop
environment Unity – with a tray bar in the top panel and the Windows 7-like
icons in the Launcher (task bar). However, it is in my experience quite buggy,
which is especially annoying when I have something that I need to get done and
it throws me out of "the flow".  Crashing applications and `Apport
<https://wiki.ubuntu.com/Apport>`_ errors belong to the daily routine. It is
actually quite embarrassing when those Apport errors appear on my mother's
computer running Ubuntu 14.04. Furthermore, the desktop has also locked several
times, forcing me to perform a hard reboot. Resizing VirtualBox causes
graphical errors quite often, forcing me to log out and in to restore the
looks of the desktop.

On a different note, I am not completely in agreement with Canonical's
direction and I dislike all politics surrounding the distribution on the
desktop side. For example do the debate about changing the default browser to
Chromium strike a nerve within me, Canonical's decision to use WebKit in the
Ubuntu Touch phone browser, their decision to develop Mir instead of adopting
Wayland, how long it took for them to abandon Upstart in favor for systemd, and
their further deviations with the upcoming Unity 8. To be frank, I find it
uncomfortable and stressful with all changes Canonical are introducing that
makes Ubuntu deviate from the other distributions.

However, I do enjoy Ubuntu as a server operating system. And Ubuntu is the most
used and well-supported Linux desktop distribution, making it easy to get help
through for example `Ask Ubuntu <http://askubuntu.com/>`_.

Fedora's niche
++++++++++++++

Where Fedora fits into the Linux distribution landscape is when you want to run
Gnome Shell, have access to reasonable up-to-date packages and a standard
release model.

Another distribution also treating Gnome Shell as a first-class citizen is
Debian. However, Debian stable's packages are much older and slow-moving than
Fedora's, since there are so many years between each Debian release. Debian
testing on the other hand offers very recent packages, but it is more of a
rolling-release distribution which slows down after its feature freeze point.
Fedora has historically released a new version every six months, which allows
them to keep its packages more up-to-date.

Fedora also has a feeling of being less opinionated than Ubuntu. Canonical
develop their own packages and try to craft their vision of a desktop operating
system, with applications with proprietary back ends such as Ubuntu One. The
Fedora team on the other hand only packages what is available upstream from
developers such as Gnome. Fedora is also strict on not allowing proprietary
applications into their repository, as opposed to Ubuntu.

Fedora does with this setup offer a great platform for developers who want
reasonable fresh packages. It is even the distro of choice for Linux's
benevolent dictator Linus Torvalds [#]_.

Customize Fedora
++++++++++++++++

Fedora only ships with open source packages in its repository – a choice that I
respect. But many people also want access to some closed source packages too,
which can be done by installing the third-party repository `RPM Fusion
<http://rpmfusion.org/>`_. It contains proprietary packages such as Nvidia's
graphics drivers and Steam. However, it also contains free software which
Fedora has not included in its own repository for `various reasons
<http://rpmfusion.org/Wishlist>`_, such as the media players `mpv
<http://mpv.io/>`_ and `SMPlayer <http://smplayer.sourceforge.net/>`_.

To get up and running easily with your preferred settings, applications and
codecs, there is a very handy script called `Fedy
<https://satya164.github.io/fedy/>`_. It installs software such as Adobe Flash,
Microsoft core fonts, RPM Fusion's repositories, multimedia codecs, Skype and
`Infinality <http://www.infinality.net>`_ for better font rendering, and it
performs tasks such as setting up sudo for the current user.

All in all it is fairly easy to extend Fedora with the most popular software.

Gnome Shell
+++++++++++

Gnome Shell works quite well out of the box, it looks nice and it does not
require a whole lot of configuration to get it right.

Plasma Desktop on the other hand, which is the most recent desktop environment
I used before returning to Gnome, looks ugly and outdated and is drowning in
options and settings. People use to say that it is no problem that Plasma
Desktop is ugly by default – because you can customize it however you want.
However, I have no desire to learn which levers I need to pull to make it look
modern and behave as other desktops.

The only things I need to do to make Gnome behave as I want is to make the Caps
Lock key behave as an additional Ctrl key using :code:`gnome-tweak-tool` and install
a few Gnome Shell extensions. The extensions I have installed are the following
ones:

- `TopIcons <https://extensions.gnome.org/extension/495/topicons/>`_.
  Displays the tray icons in the right side of the top bar.

- `TaskBar <https://extensions.gnome.org/extension/584/taskbar/>`_. Shows
  the icons of the running applications in the left side of the top bar.

- `Workspace indicator
  <https://extensions.gnome.org/extension/21/workspace-indicator/>`_. Shows the
  current workspace in the top panel.

- `Fripery Move Clock <https://extensions.gnome.org/extension/2/move-clock/>`_.
  Moves the clock from being located in the center of the top panel to its
  right side.

These extensions are depicted in the screenshot below. The wallpaper is one of
the preinstalled ones.

.. image:: {filename}/images/gnome-shell.jpg
   :alt: Screenshot of my Gnome Shell setup
   :align: center
   :class: img-responsive

Concluding thoughts
+++++++++++++++++++

By running Fedora it feels quite relieving to stand outside Ubuntu's politics
and Arch Linux's constant movement.

I have had a mostly pleasant experience with Fedora so far, however, only time
can tell whether it will satisfy my needs. I distro jump quite often, so I can
not guarantee that I will stay if I were to encounter too many obstacles. My
fear is that developers of exotic applications might not release packages or
instructions for Fedora; I have already encountered a project that only
provided compilation instructions for Debian based systems. But I certainly
hope that it will fulfill my future expectations, and I am looking forward to
the upcoming release of Fedora, version 21, which is landing in December.

References
++++++++++

.. [#] Interview with Linus Torvalds from Linux Format 163 (2012). *TuxRadar*.
   http://www.tuxradar.com/content/interview-linus-torvalds-linux-format-163
   (2014-11-04).
