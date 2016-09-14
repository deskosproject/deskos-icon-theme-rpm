%global commit 1462edf656c1757abe2fb3806dc0fe5e11e45177
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           deskos-icon-theme
Version:        0.1
Release:        1%{?dist}
Summary:        Defaults icons for DeskOS

License:        CC-BY-SA
URL:            https://github.com/deskosproject/deskos-icon-theme-rpm

# Downloaded from https://github.com/sljunkie/adwaita-blue/tarball/%{commit}
Source0:        https://dl.deskosproject.org/sources/deskos-icon-theme/sljunkie-adwaita-blue-%{shortcommit}.tar.gz
Patch0:         deskos-name.patch

BuildArch:      noarch
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme

%description
Default icons for DeskOS, based on Adwaita Blue by sljunkie.
Adwaita Blue is a minimal icon theme based on Cheser by chekavy whose
aim is to serve only as a 'blue folder' variation on the stock GNOME
icon theme Adwaita. Plus a few mimetypes and device icons that fit the
original icon theme look and feel.

%prep
%setup -q -n sljunkie-adwaita-blue-%{shortcommit}
%patch0 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/DeskOS
cp -pr 16x16 22x22 24x24 32x32 48x48 256x256 %{buildroot}%{_datadir}/icons/DeskOS
cp -p index.theme %{buildroot}%{_datadir}/icons/DeskOS

%post
touch --no-create %{_datadir}/icons/DeskOS &>/dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/DeskOS &>/dev/null
  gtk-update-icon-cache -q %{_datadir}/icons/DeskOS &>/dev/null ||:
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/DeskOS &>/dev/null ||:

%files
%doc README.md
%license COPYING
%{_datadir}/icons/DeskOS

%changelog
* Fri Apr 15 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Intial rpm build
