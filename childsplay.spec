Summary: 	Games for children with plugins
Name: 		childsplay
Version: 	1.5.1
Release: 	%mkrel 1
Source0: 	http://prdownloads.sourceforge.net/childsplay/%{name}-%{version}.tgz
Patch0:		setup.py.diff
URL: 		http://childsplay.sourceforge.net/
License: 	GPLv3
Group: 		Games/Other
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	python
Requires: 	pygame
Requires:	python-numpy
Requires:	pygtk2.0
Requires:	python-sqlalchemy
BuildArch:	noarch

%description
Childsplay is a 'suite' of educational games for young children. It's written
in Python and uses the SDL-libraries to make it more games-like then, for
instance, gcompris. The aim is to be educational and at the same time be fun
to play.

NOTE: This package includes all games currently available for childsplay.

%prep
%setup -q
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT

PREFIX=%buildroot%_prefix python setup.py install --root="%buildroot" --optimize=1

%find_lang %{name} --all-name

rm -fr %buildroot%_datadir/doc/*

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Games for children with plugins
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;KidsGame;
EOF

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps
install -p -m 644 lib/SPData/menu/default/logo_cp_32x32.png \
  $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -p -m 644 lib/SPData/menu/default/logo_cp_64x64.png \
  $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README* doc/*
%{_bindir}/*
%{_datadir}/childsplay_sp
%{_datadir}/sp_alphabetsounds
%{_datadir}/applications/*.desktop
%py_puresitedir/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
