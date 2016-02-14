%define tarname	AriaSrc
%define debug_package %{nil}
Name:		ariamaestosa
Version:	1.4.11
Release:	1
Summary:	An open-source midi tracker/editor
# License is GPLv2 with exceptions (look at license.txt)
License:	GPLv2
Group:		Sound
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
BuildRequires:	wxgtku3.0-devel
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

