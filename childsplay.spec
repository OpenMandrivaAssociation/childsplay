%define name 	childsplay
%define version 0.90.1
%define release %mkrel 4

%define pluginsver 0.90

Summary: 	Games for children with plugins
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://prdownloads.sourceforge.net/childsplay/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/childsplay/%{name}_plugins-%{pluginsver}.tar.bz2
Patch1:		childsplay-0.81.8-highscore.patch
URL: 		http://childsplay.sourceforge.net/
License: 	GPLv3
Group: 		Games/Other
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	python-devel 
Requires: 	pygame
BuildArch:	noarch

%description
Childsplay is a 'suite' of educational games for young children. It's written
in Python and uses the SDL-libraries to make it more games-like then, for
instance, gcompris. The aim is to be educational and at the same time be fun
to play.

NOTE: This package includes all games currently available for childsplay.

%prep
%setup -q -b 1
%patch1 -p1

# we don't use the buggy provided install
rm install.py
# the translation is merged into the assetml file, so don't ship it seperatly
rm -r assetml/childsplay/memory-136x136/po
# fixup the python scripts to call python directly and make them executable
sed -i 's!/usr/bin/env python!%{_bindir}/python!' %{name}.py letters-trans.py
chmod 755 %{name}.py letters-trans.py pyassetmlcreator.py
# move these out of Data so our wildcard install doesn't install them
mv Data/*.txt Data/logo_cp_*.png Data/childsplay.* .

%build
# INSTALL.sh is seriously borked, so DIY
echo "## Automated file please do not edit" > BASEPATH.py
echo "CPDIR=\"%{_datadir}/%{name}\"" >> BASEPATH.py  
echo "SHAREDATADIR=\"%{_datadir}/%{name}/Data\"" >> BASEPATH.py
echo "SHARELIBDATADIR=\"%{_datadir}/%{name}/plugins\"" >> BASEPATH.py
echo "LIBDIR=\"%{_datadir}/%{name}/plugins\"" >> BASEPATH.py
echo "MODULESDIR=\"%{_datadir}/%{name}/plugins\"" >> BASEPATH.py
echo "RCDIR=\"%{_datadir}/%{name}/plugins/ConfigData\"" >> BASEPATH.py
echo "LOCALEDIR=\"%{_datadir}/locale\"" >> BASEPATH.py
echo "ASSETMLDIR=\"%{_datadir}\"" >> BASEPATH.py
echo "CHILDSPLAYRC=\"childsplayrc\"" >> BASEPATH.py
echo "HOME_DIR_NAME=\".childsplay\"" >> BASEPATH.py

%install
rm -rf $RPM_BUILD_ROOT
# INSTALL.sh is seriously borked, so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
cp -a *.py  $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s ../share/%{name}/%{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s ../share/%{name}/letters-trans.py \
  $RPM_BUILD_ROOT%{_bindir}/letters-trans
cp -a Data  $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a lib/* $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
cp -a assetml/%{name}/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a locale/* $RPM_BUILD_ROOT%{_datadir}/locale
cp -a man/* $RPM_BUILD_ROOT%{_mandir}/man6

# childsplay_plugins stuff
cd ../childsplay_plugins-%{pluginsver}
cp -a Data/*.icon.png $RPM_BUILD_ROOT%{_datadir}/childsplay/Data/icons
cp -a lib/* $RPM_BUILD_ROOT%{_datadir}/childsplay/plugins
cp -a assetml/childsplay/* $RPM_BUILD_ROOT%{_datadir}/childsplay
cd -

%find_lang %{name}

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

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps
install -p -m 644 logo_cp_16x16.png \
  $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -p -m 644 logo_cp_32x32.png \
  $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -p -m 644 logo_cp_48x48.png \
  $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

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
%defattr(-, root, root, -)
%doc README* doc/GPL* doc/README* License_*.ttf.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
