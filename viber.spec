# TODO
# - need to chown $USER /usr/lib/viber or app won't start
Summary:	Viber - Free Calls and Messages
Name:		viber
# Version from About dialog
Version:	3.1.2
Release:	0.4
License:	?
Group:		Applications/Communications
Source0:	http://download.cdn.viber.com/cdn/desktop/Linux/%{name}.deb
# NoSource0-md5:	7be88e0d854aa31e0d7dade32a6413a8
NoSource:	0
Patch0:		desktop.patch
URL:		http://viber.com/products/linux
BuildRequires:	desktop-file-utils
Requires:	desktop-file-utils
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/%{name}

# list of files (regexps) which don't generate Provides
%define		_noautoprovfiles	%{_appdir}

%define		req_qt5		libQt5Core.so.5 libQt5DBus.so.5 libQt5Gui.so.5 libQt5Network.so.5 libQt5OpenGL.so.5 libQt5PrintSupport.so.5 libQt5Qml.so.5 libQt5Quick.so.5 libQt5Sql.so.5 libQt5Svg.so.5 libQt5V8.so.5 libQt5WebKit.so.5 libQt5WebKitWidgets.so.5 libQt5Widgets.so.5
%define		req_x11		libXss.so.1
%define		req_bfd		libbfd-2.22-system.so
%define		req_icu		libicudata.so.48 libicui18n.so.48 libicuuc.so.48

%define		_noautoreq  %{req_qt5} %{req_x11} %{req_bfd} %{req_icu}

%description
Viber for Linux lets you send free messages and make free calls to
other Viber users on any device and network, in any country! Viber
syncs your contacts and messages with your mobile device.

- Text, photo and sticker messages
- Group conversations
- Call any Viber user for free
- Full sync between your mobile and your Linux
- Transfer ongoing calls between your mobile and your desktop
- No registration, passwords or invitations required

%prep
%setup -qcT
ar x %{SOURCE0}
tar xzf data.tar.gz
mv .%{_datadir}/* .
mv viber/Viber.sh .
mv viber/{V,v}iber

%patch0 -p1

cat <<'EOF' > viber.sh
#!/bin/sh
export LD_LIBRARY_PATH=%{_appdir}:$LD_LIBRARY_PATH
exec %{_appdir}/viber "$@"
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_pixmapsdir},%{_desktopdir}}
cp -a viber/* $RPM_BUILD_ROOT%{_appdir}
cp -p applications/viber.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p pixmaps/viber.png $RPM_BUILD_ROOT%{_pixmapsdir}
install -p viber.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/viber
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/viber
%attr(755,root,root) %{_appdir}/libViber.so
%{_appdir}/Sound
%{_appdir}/icons
%{_appdir}/viber.png
%{_desktopdir}/viber.desktop
%{_pixmapsdir}/viber.png

# qt5
%attr(755,root,root) %{_appdir}/libQt5Network.so.5
%attr(755,root,root) %{_appdir}/libQt5Svg.so.5
%attr(755,root,root) %{_appdir}/libQt5V8.so.5
%attr(755,root,root) %{_appdir}/libQt5Gui.so.5
%attr(755,root,root) %{_appdir}/libQt5PrintSupport.so.5
%attr(755,root,root) %{_appdir}/libQt5Qml.so.5
%attr(755,root,root) %{_appdir}/libQt5Widgets.so.5
%attr(755,root,root) %{_appdir}/libQt5OpenGL.so.5
%attr(755,root,root) %{_appdir}/libQt5WebKit.so.5
%attr(755,root,root) %{_appdir}/libQt5DBus.so.5
%attr(755,root,root) %{_appdir}/libQt5Sql.so.5
%attr(755,root,root) %{_appdir}/libQt5WebKitWidgets.so.5
%attr(755,root,root) %{_appdir}/libQt5Core.so.5
%attr(755,root,root) %{_appdir}/libQt5Quick.so.5
# qt5 plugins
%dir %{_appdir}/platforms
%attr(755,root,root) %{_appdir}/platforms/libqxcb.so
%attr(755,root,root) %{_appdir}/platforms/libqlinuxfb.so
%attr(755,root,root) %{_appdir}/platforms/libqminimal.so
%dir %{_appdir}/sqldrivers
%attr(755,root,root) %{_appdir}/sqldrivers/libqsqlite.so
%dir %{_appdir}/imageformats
%attr(755,root,root) %{_appdir}/imageformats/libqmng.so
%attr(755,root,root) %{_appdir}/imageformats/libqtga.so
%attr(755,root,root) %{_appdir}/imageformats/libqwbmp.so
%attr(755,root,root) %{_appdir}/imageformats/libqjpeg.so
%attr(755,root,root) %{_appdir}/imageformats/libqtiff.so
%attr(755,root,root) %{_appdir}/imageformats/libqsvg.so
%attr(755,root,root) %{_appdir}/imageformats/libqgif.so
%attr(755,root,root) %{_appdir}/imageformats/libqico.so

# icu
%attr(755,root,root) %{_appdir}/libicudata.so.48
%attr(755,root,root) %{_appdir}/libicui18n.so.48
%attr(755,root,root) %{_appdir}/libicuuc.so.48

# x11
%attr(755,root,root) %{_appdir}/libXss.so.1

# binutils
%attr(755,root,root) %{_appdir}/libbfd-2.22-system.so
