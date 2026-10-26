%global		debug_package %{nil}

%define		tarname	AriaSrc

Summary:	An open-source midi tracker/editor
Name:	ariamaestosa
Version:	1.4.13
Release: 1
# License is GPLv2 with exceptions (look at license.txt)
License:	GPL-2.0-or-later
Group:		Sound
Url:		https://ariamaestosa.sourceforge.net
# See also: https://github.com/ariamaestosa/ariamaestosa
Source0:	https://sourceforge.net/projects/ariamaestosa/files/%{name}/%{version}/%{tarname}-%{version}.tar.bz2
Source1:	ariamaestosa.desktop
# TODO: Valutate patches from https://github.com/manta89640/sxfmustool
Patch0:	ariamaestosa-1.4.13-python3-fixes.patch
Patch1:	ariamaestosa-1.4.13-fix-namespace-error-for-Editor.patch
Patch2:	ariamaestosa-1.4.13-remove-once-macro.patch
Patch3:	ariamaestosa-1.4.13-fix-linking-error.patch
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	imagemagick
BuildRequires:	rcs
BuildRequires:	scons
BuildRequires:	swig
BuildRequires:	ghostscript-devel
BuildRequires:	wxgtku3.2-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(glu)

%description
Aria Maestosa is an open-source (GPL) midi tracker/editor. It lets you
compose, edit and play midi files with a few clicks in a user-friendly
interface offering keyboard, guitar, drum and controller views.

%files -f aria_maestosa.lang
%doc Changelog.txt TODO.txt license.txt
%doc Documentation/*
%{_bindir}/Aria
%{_datadir}/Aria/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{tarname}-%{version}

# FIXME: scons has troubles with the directories in Resources:
# workaround by moving them and install their stuff manually
mv Resources/Documentation .
mv Resources/score .

# Fix FSF address
sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/31 Milk Street, # 960789, Boston, MA 02196, USA/g' license.txt


%build
%scons prefix=%{_prefix} destdir=%{buildroot} platform=linux renderer=opengl WXCONFIG=%{_bindir}/wx-config LDFLAGS="-lwx_gtk3u_webview-3.2" CXXFLAGS="-fPIC"


%install
%scons_install prefix=%{buildroot}%{_prefix} platform=linux 

# Install manually
mkdir -p %{buildroot}%{_datadir}/Aria/score
cp score/* %{buildroot}%{_datadir}/Aria/score

# Provide more icons
for SIZE in 16x16 22x22 32x32 48x48 64x64 128x128; do
	mkdir -p %{buildroot}%{_iconsdir}/hicolor/$SIZE/apps
	convert aria128.png -geometry $SIZE %{buildroot}%{_iconsdir}/hicolor/$SIZE/apps/%{name}.png
done

# Provide our desktop-menu entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=0644 --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Fix perms and rpath for main binary
chmod 755 %{buildroot}%{_bindir}/Aria
chrpath -d  %{buildroot}%{_bindir}/Aria

%find_lang aria_maestosa
