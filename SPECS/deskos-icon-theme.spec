%global commit 1462edf656c1757abe2fb3806dc0fe5e11e45177
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           deskos-icon-theme
Version:        0.1
Release:        1
Summary:        Icons for the DeskOS Project
License:        GPLv2
URL:            https://deskosproject.org
Source0:        https://github.com/sljunkie/adwaita-blue/tarball/%{commit}
BuildArch:      noarch
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme

%description
This is a minimal icon theme based on Cheser by chekavy whose aim is to
serve only as a 'blue folder' variation on the stock GNOME icon theme
Adwaita. Plus a few mimetypes and device icons that fit the original
icon theme look and feel.

%prep
%setup -q -n sljunkie-adwaita-blue-%{shortcommit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/deskos
cp -pr *x* %{buildroot}%{_datadir}/icons/deskos
cp -p index.theme %{buildroot}%{_datadir}/icons/deskos

%post
touch --no-create %{_datadir}/icons/deskos &>/dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/deskos &>/dev/null
  gtk-update-icon-cache -q %{_datadir}/icons/deskos &>/dev/null ||:
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/deskos &>/dev/null ||:

%files
%doc README.md
%license COPYING
%{_datadir}/icons/deskos

%changelog
* Fri Apr 15 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Intial rpm build
