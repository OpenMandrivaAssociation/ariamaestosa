%define tarname	AriaSrc

Name:		ariamaestosa
Version:	1.4.11
Release:	%mkrel 3
Summary:	An open-source midi tracker/editor
# License is GPLv2 with exceptions (look at license.txt)
License:	GPLv2
Group:		Sound/Midi
URL:		http://ariamaestosa.sourceforge.net
Source0:	http://sourceforge.net/projects/ariamaestosa/files/%{name}/%{version}/%{tarname}-%{version}.tar.bz2
Source1:	ariamaestosa.desktop
BuildRequires:	cvs
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	imagemagick
BuildRequires:	rcs
BuildRequires:	scons
BuildRequires:	swig
BuildRequires:	ghostscript-devel
BuildRequires:	wxgtk3.0-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)

%description
Aria Maestosa is an open-source (GPL) midi tracker/editor. It lets you
compose, edit and play midi files with a few clicks in a user-friendly
interface offering keyboard, guitar, drum and controller views.


%prep
%setup -q -n %{tarname}-%{version}

%build
%{__python} scons/scons.py prefix=%{_prefix} destdir=%{buildroot}

%install
%{__python} scons/scons.py install prefix=%{buildroot}%{_prefix}

%find_lang aria_maestosa

# icons-repertory .png
for SIZE in 16x16 22x22 32x32 48x48 64x64 128x128; do
	mkdir -p %{buildroot}%{_iconsdir}/hicolor/$SIZE/apps
	convert aria128.png -geometry $SIZE %{buildroot}%{_iconsdir}/hicolor/$SIZE/apps/%{name}.png
done

# desktop menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=0644 --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f aria_maestosa.lang
%doc Changelog.txt TODO.txt license.txt
%attr(0755,root,root) %{_bindir}/Aria
%{_datadir}/Aria/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Sat Feb 13 2016 umeabot <umeabot> 1.4.11-3.mga6
+ Revision: 959519
- Mageia 6 Mass Rebuild

* Fri Aug 14 2015 ycantin <ycantin> 1.4.11-2.mga6
+ Revision: 864690
- rebuild for new wxgtk built with wxRE_ADVANCED
- typo

* Tue Aug 04 2015 daviddavid <daviddavid> 1.4.11-1.mga6
+ Revision: 861026
- new version: 1.4.11

* Wed Jul 22 2015 daviddavid <daviddavid> 1.4.10-4.mga6
+ Revision: 856226
- rebuild for new wxgtk built with gtk3

* Wed Oct 15 2014 umeabot <umeabot> 1.4.10-3.mga5
+ Revision: 740954
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 1.4.10-2.mga5
+ Revision: 677894
- Mageia 5 Mass Rebuild

* Thu Aug 14 2014 daviddavid <daviddavid> 1.4.10-1.mga5
+ Revision: 662474
- new version: 1.4.10

* Mon Jul 28 2014 daviddavid <daviddavid> 1.4.9-1.mga5
+ Revision: 657818
- imported package ariamaestosa

