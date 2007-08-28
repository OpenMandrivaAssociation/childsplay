%define name 	childsplay
%define version 0.90.1
%define release %mkrel 1

%define pluginsver 0.90
# look in childsplay-plugins-0.xx/install.sh for variable $SCORE
%define score 	Packid,Numbers

Summary: 	Games for children with plugins
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://prdownloads.sourceforge.net/childsplay/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/childsplay/%{name}_plugins-%{pluginsver}.tar.bz2
Patch0:		childsplay.INSTALL.SH.patch
URL: 		http://childsplay.sourceforge.net/
License: 	GPLv3
Group: 		Games/Other
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	python-devel 
Requires: 	pygame
Buildarch:	noarch

%description
Childsplay is a 'suite' of educational games for young children. It's written
in Python and uses the SDL-libraries to make it more games-like then, for
instance, gcompris. The aim is to be educational and at the same time be fun
to play.

NOTE: This package includes all games currently available for childsplay.

%prep

%setup -q -b 1

%patch0 -p 1

%build
%install
rm -rf $RPM_BUILD_ROOT
# fix python compile error
perl -p -i -e 's/quiet\=1//g' install.py

#install main
mkdir -p %buildroot/%_bindir
echo "#!/bin/sh" > $RPM_BUILD_ROOT/usr/bin/childsplay
echo "python %_libdir/%name/childsplay.py \$\*" >> $RPM_BUILD_ROOT/usr/bin/childsplay
chmod +x $RPM_BUILD_ROOT/usr/bin/childsplay
mkdir -vp $RPM_BUILD_ROOT/%_libdir/%name
cp -rf *.py $RPM_BUILD_ROOT/%_libdir/%name
cp -rf Data $RPM_BUILD_ROOT/%_libdir/%name
chmod 0666 $RPM_BUILD_ROOT/%_libdir/%name/Data/*score
cp -rf lib $RPM_BUILD_ROOT/%_libdir/%name
mkdir -p $RPM_BUILD_ROOT/%_mandir/man6
cp -rf man/childsplay.6.gz $RPM_BUILD_ROOT/%_mandir/man6
mkdir -p $RPM_BUILD_ROOT/%_datadir/locale
cp -rf locale/* $RPM_BUILD_ROOT/%_datadir/locale

# compile bytecode
python install.py --compile %_libdir/%name
python install.py --compile %_libdir/%name/lib
python install.py --makedir %_libdir/%name/lib

# fix symlinks
#rm -f $RPM_BUILD_ROOT/%_libdir/%name/lib/LettersData/*
#cp $RPM_BUILD_ROOT/%_libdir/%name/lib/MemoryData/* $RPM_BUILD_ROOT/%_libdir/%name/lib/LettersData/

cp -rf assetml $RPM_BUILD_ROOT/usr/share
# install plugins
pushd ../%{name}_plugins-%pluginsver
python $RPM_BUILD_ROOT/%_libdir/%name/install.py --compile `pwd`/lib
cp -rf `pwd`/lib/* $RPM_BUILD_ROOT/%_libdir/%name/lib
cp -rf `pwd`/Data/*.icon.png $RPM_BUILD_ROOT/%_libdir/%name/Data/icons
#cp -rf `pwd`/locale/* $RPM_BUILD_ROOT/%_datadir/locale
#python add-score.py $RPM_BUILD_ROOT/%_libdir/%name %score
cp -rf assetml $RPM_BUILD_ROOT/usr/share

#fix lang files atributes
chmod 644 $RPM_BUILD_ROOT%_datadir/locale/fr/LC_MESSAGES/*
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Games for children with plugins
Exec=%{name}
Icon=amusement_section.png
Terminal=false
Type=Application
Categories=Game;KidsGame;
EOF

popd
%find_lang %{name}
chmod ugo+r -R doc/
cat << EOF >$RPM_BUILD_ROOT/%_libdir/%name/BASEPATH.py
BASEPATH = "%_prefix" 
EXECDIR = "%_bindir"
LOCALEDIR = "%_datadir/locale" 
ASSETMLDIR = "%_datadir/assetml"
SCOREDIR = "/var/games"
SCOREFILE = SCOREDIR + "/childsplay.score"
DOCDIR = BASEPATH + "/share/doc/" 
MANDIR = "%_mandir/man6"
CPDIR = "%_prefix/lib/%name"
SHAREDIR = CPDIR 
BINDIR = "%_gamesbindir"
LIBDIR = CPDIR + "/lib/" 
MODULESDIR = LIBDIR
SHARELIBDATADIR = SHAREDIR + "/lib"
SHAREDATADIR = SHAREDIR + "/Data"
RCDIR = SHARELIBDATADIR + "/ConfigData"
CHILDSPLAYRC = "childsplayrc" 
HOME_DIR_NAME = ".childplayrc"
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc doc/*
%_bindir/%name
%_libdir/%name
%_datadir/assetml/%name/
%_mandir/man6/*
%_datadir/applications/*
