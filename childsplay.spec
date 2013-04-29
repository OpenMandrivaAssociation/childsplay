%global alphabet_ver 0.9.1

Summary: 	Games for children with plugins
Name: 		childsplay
Version: 	1.6
Release: 	2
Source0: 	http://downloads.sourceforge.net/schoolsplay/%{name}-%{version}.tgz
Source10:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_bg-%{alphabet_ver}.tgz
Source11:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_ca-%{alphabet_ver}.tgz
Source12:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_de-%{alphabet_ver}.tgz
Source13:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_el-0.9.tgz
Source14:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_en_GB-%{alphabet_ver}.tgz
Source15:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_es-%{alphabet_ver}.tgz
Source16:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_fr-%{alphabet_ver}.tgz
Source17:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_it-%{alphabet_ver}.tgz
Source18:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_lt-%{alphabet_ver}.tgz
Source19:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_nb-%{alphabet_ver}.tgz
Source20:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_nl-%{alphabet_ver}.tgz
Source21:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_pt-%{alphabet_ver}.tgz
Source22:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_pt_BR-%{alphabet_ver}.tgz
Source23:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_ro-%{alphabet_ver}.tgz
Source24:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_ru-%{alphabet_ver}.tgz
Source25:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_sl-%{alphabet_ver}.tgz
Source26:       http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_sv-0.9.2.tgz
Patch0:		setup.py.diff
URL: 		http://childsplay.sourceforge.net/
License: 	GPLv3
Group: 		Education
BuildRequires: 	python
Requires: 	pygame
Requires:	python-numpy
Requires:	pygtk2.0
Requires:	python-sqlalchemy
BuildArch:	noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-buildroot
Requires:	%{name}-sound = %{version}-%{release}

%description
Childsplay is a 'suite' of educational games for young children. It's written
in Python and uses the SDL-libraries to make it more games-like then, for
instance, GCompris. The aim is to be educational and at the same time be fun
to play.

NOTE: This package includes all games currently available for childsplay.
Some activities make use of language dependent voice samples, these sounds are
available as childsplay-sounds packages. For those you'll have to
install the childsplay-alphabet_sounds package for the languages you intend to
use. For example childsplay-sounds-pt_BR.

%package sounds-bg
Summary:        Bulgarian alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-bg
Bulgarian alphabet sounds for Childsplay


%package sounds-ca
Summary:        Catalan alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-ca
Catalan alphabet sounds for Childsplay


%package sounds-de
Summary:        German alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-de
German alphabet sounds for Childsplay


%package sounds-el
Summary:        New Greek alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-el
new Greek alphabet sounds for Childsplay


%package sounds-en_GB
Summary:        British English alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-en_GB
British English alphabet sounds for Childsplay


%package sounds-es
Summary:        Spanish alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-es
Spanish alphabet sounds for Childsplay


%package sounds-fr
Summary:        French alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-fr
French alphabet sounds for Childsplay


%package sounds-it
Summary:        Italian alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-it
Italian alphabet sounds for Childsplay


%package sounds-lt
Summary:        Lithuanian alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-lt
Lithuanian alphabet sounds for Childsplay


%package sounds-nb
Summary:        Norwegian Bokmål alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-nb
Norwegian Bokmål alphabet sounds for Childsplay


%package sounds-nl
Summary:        Dutch alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-nl
Dutch alphabet sounds for Childsplay


%package sounds-pt
Summary:        Portuguese alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-pt
Portuguese alphabet sounds for Childsplay


%package sounds-pt_BR
Summary:        Brazilian portuguese alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-pt_BR
Brazilian portuguese alphabet sounds for Childsplay


%package sounds-ro
Summary:        Romanian alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-ro
Romanian alphabet sounds for Childsplay


%package sounds-ru
Summary:        Russian alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-ru
Russian alphabet sounds for Childsplay


%package sounds-sl
Summary:        Slovenian alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-sl
Slovenian alphabet sounds for Childsplay


%package sounds-sv
Summary:        Swedish alphabet sounds for Childsplay
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}
Provides: %{name}-sound = %{version}-%{release} 
%description sounds-sv
Swedish alphabet sounds for Childsplay

%prep
%setup -q -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24 -a 25 -a 26
%patch0 -p0

%install
rm -rf %{buildroot}

PREFIX=%{buildroot}%{_prefix} python setup.py install --root="%{buildroot}" --optimize=1

%find_lang %{name} --all-name

rm -fr %{buildroot}%{_datadir}/doc/*

# below is the desktop file and icon stuff.
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{_real_vendor}-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Games for children
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Education;
EOF

mkdir -p %{buildroot}%{_iconsdir}/hicolor/32x32/apps
mkdir -p %{buildroot}%{_iconsdir}/hicolor/64x64/apps
install -p -m 644 lib/SPData/menu/default/logo_cp_32x32.png \
  %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -p -m 644 lib/SPData/menu/default/logo_cp_64x64.png \
  %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png

#Alphabet sounds
# mkdir -p %{buildroot}%{_datadir}/%{name}/CPData/FlashcardsData/names
for sounds in bg ca de en_GB es fr it nb nl pt pt_BR ro ru sl 
do
  cp -a alphabet_sounds_$sounds-%{alphabet_ver}/AlphabetSounds/$sounds %{buildroot}%{_datadir}/sp_alphabetsounds
done
for sounds in ca de es fr it nl pt_BR ru sl
do
  cp -a alphabet_sounds_$sounds-%{alphabet_ver}/FlashCardsSounds/$sounds %{buildroot}%{_datadir}/%{name}_sp/CPData/FlashcardsData/names
done
#some language are not sync
cp -a alphabet_sounds_el-0.9/AlphabetSounds/el %{buildroot}%{_datadir}/sp_alphabetsounds
cp -a alphabet_sounds_sv-0.9.2/AlphabetSounds/sv %{buildroot}%{_datadir}/sp_alphabetsounds
cp -a alphabet_sounds_lt-0.9.1/AlphabetSounds %{buildroot}%{_datadir}/sp_alphabetsounds/lt

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README* doc/*
%{_bindir}/*
%{_datadir}/childsplay_sp/SPData
# %{_datadir}/childsplay_sp/CPData
%{_datadir}/childsplay_sp/CPData/*.*
%{_datadir}/childsplay_sp/CPData/BilliardData
%{_datadir}/childsplay_sp/CPData/FallinglettersData
%{_datadir}/childsplay_sp/CPData/FindsoundData
%{_datadir}/childsplay_sp/CPData/FishtankData
%{_datadir}/childsplay_sp/CPData/FlashcardsData/cards
%{_datadir}/childsplay_sp/CPData/FlashcardsData/sounds
%{_datadir}/childsplay_sp/CPData/FlashcardsData/names/en
%{_datadir}/childsplay_sp/CPData/LMemoryData
%{_datadir}/childsplay_sp/CPData/MemoryData
%{_datadir}/childsplay_sp/CPData/PackidData
%{_datadir}/childsplay_sp/CPData/PongData
%{_datadir}/childsplay_sp/CPData/PuzzleData
%{_datadir}/childsplay_sp/CPData/SoundmemoryData
%{_datadir}/sp_alphabetsounds/en
%{_datadir}/applications/*.desktop
%{py_puresitedir}/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files sounds-bg
%defattr(-, root, root, -)
%doc  alphabet_sounds_bg-%{alphabet_ver}/GPL-2  alphabet_sounds_bg-%{alphabet_ver}/README
%{_datadir}/sp_alphabetsounds/bg

%files sounds-ca
%defattr(-, root, root, -)
%doc  alphabet_sounds_ca-%{alphabet_ver}/copyright  alphabet_sounds_ca-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/ca
%{_datadir}/sp_alphabetsounds/ca

%files sounds-de
%defattr(-, root, root, -)
%doc  alphabet_sounds_de-%{alphabet_ver}/copyright  alphabet_sounds_de-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/de
%{_datadir}/sp_alphabetsounds/de

%files sounds-el
%defattr(-, root, root, -)
%doc  alphabet_sounds_el-0.9/copyright  alphabet_sounds_el-0.9/GPL-2
%{_datadir}/sp_alphabetsounds/el

%files sounds-en_GB
%defattr(-, root, root, -)
%doc  alphabet_sounds_en_GB-%{alphabet_ver}/copyright  alphabet_sounds_en_GB-%{alphabet_ver}/GPL-2
%{_datadir}/sp_alphabetsounds/en_GB

%files sounds-es
%defattr(-, root, root, -)
%doc  alphabet_sounds_es-%{alphabet_ver}/copyright  alphabet_sounds_es-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/es
%{_datadir}/sp_alphabetsounds/es

%files sounds-fr
%defattr(-, root, root, -)
%doc  alphabet_sounds_fr-%{alphabet_ver}/copyright  alphabet_sounds_fr-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/fr
%{_datadir}/sp_alphabetsounds/fr

%files sounds-it
%defattr(-, root, root, -)
%doc  alphabet_sounds_it-%{alphabet_ver}/copyright  alphabet_sounds_it-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/it
%{_datadir}/sp_alphabetsounds/it

%files sounds-lt
%defattr(-, root, root, -)
%doc  alphabet_sounds_lt-%{alphabet_ver}/copyright  alphabet_sounds_lt-%{alphabet_ver}/GPL-2
%{_datadir}/sp_alphabetsounds/lt

%files sounds-nb
%defattr(-, root, root, -)
%doc  alphabet_sounds_nb-%{alphabet_ver}/copyright  alphabet_sounds_nb-%{alphabet_ver}/GPL-2
%{_datadir}/sp_alphabetsounds/nb

%files sounds-nl
%defattr(-, root, root, -)
%doc  alphabet_sounds_nl-%{alphabet_ver}/copyright  alphabet_sounds_nl-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/nl
%{_datadir}/sp_alphabetsounds/nl

%files sounds-ro
%defattr(-, root, root, -)
%doc  alphabet_sounds_ro-%{alphabet_ver}/copyright  alphabet_sounds_ro-%{alphabet_ver}/GPL-2
%{_datadir}/sp_alphabetsounds/ro

%files sounds-pt
%defattr(-, root, root, -)
%doc  alphabet_sounds_pt-%{alphabet_ver}/copyright  alphabet_sounds_pt-%{alphabet_ver}/GPL-2
%{_datadir}/sp_alphabetsounds/pt

%files sounds-pt_BR
%defattr(-, root, root, -)
%doc  alphabet_sounds_pt_BR-%{alphabet_ver}/copyright  alphabet_sounds_pt_BR-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/pt_BR
%{_datadir}/sp_alphabetsounds/pt_BR

%files sounds-ru
%defattr(-, root, root, -)
%doc  alphabet_sounds_ru-%{alphabet_ver}/copyright  alphabet_sounds_ru-%{alphabet_ver}/GPL-2
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/ru
%{_datadir}/sp_alphabetsounds/ru

%files sounds-sl
%defattr(-, root, root, -)
%doc  alphabet_sounds_sl-%{alphabet_ver}/LICENCE  alphabet_sounds_sl-%{alphabet_ver}/README
%{_datadir}/sp_alphabetsounds/sl
%{_datadir}/%{name}_sp/CPData/FlashcardsData/names/sl

%files sounds-sv
%defattr(-, root, root, -)
%doc  alphabet_sounds_sv-0.9.2/copyright  alphabet_sounds_sv-0.9.2/GPL-2
%{_datadir}/sp_alphabetsounds/sv

