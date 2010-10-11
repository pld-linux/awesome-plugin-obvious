
%define		rel 20100925
Summary:	Set of obvious awesome widgets
Summary(hu.UTF-8):	Alapvető awesome widget-ek gyűjteménye
Summary(pl.UTF-8):	Zestaw oczywistych widgetów dla awesome
Name:		awesome-plugin-obvious
Version:	0
Release:	0.%{rel}.2
License:	MIT
Group:		X11/Window Managers
# git clone git://git.mercenariesguild.net/obvious.git
Source0:	http://carme.pld-linux.org/~uzsolt/sources/obvious-%{rel}.tar.bz2
# Source0-md5:	a3f4b58138e446cddd28b87ab6dc86b0
URL:		http://awesome.naquadah.org/wiki/Obvious
Requires:	awesome
Requires:	awesome-plugin-naughty
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Obvious is a set of awesome widgets like prompt, alsa volume control
etc.

%description -l hu.UTF-8
Obvious awesome widget-ek tömkelege, mint prompt, alsa
hangerőszabályzás, stb.

%description -l pl.UTF-8
Obvious jest zestawem widgetów dla awesome takich jak prompt, kontrola
głośności alsa i tym podobne.

%prep
%setup -q -n obvious-%{rel}

for I in $(find -name *.md); do
  mv $I $(echo $I | sed "s@\.md\$@@")
done
for I in */readme; do
  mv $I readme-$(dirname $I)
done

%install
rm -rf $RPM_BUILD_ROOT

SUBMODULES=battery,fs_usage,io,net,wlan,basic_mpd,clock,cpu,mem,popup_run_prompt,volume_alsa

install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/obvious
install init.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/obvious
cp -a {lib,$SUBMODULES} $RPM_BUILD_ROOT%{_datadir}/awesome/lib/obvious

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING LICENSE TODO readme-*
%{_datadir}/awesome/lib/obvious
