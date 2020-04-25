%define engine  wyrmgus

Name:           wyrmsun
Version:        3.5.4
Release:        1
Summary:        Real-time strategy game based on history, mythology and fiction
Group:          Games/Strategy
License:        GPLv2+ and CC-BY-SA
URL:            http://www.indiedb.com/games/wyrmsun
Source0:        https://github.com/andrettin/wyrmgus/archive/v%{version}/%{engine}-%{version}.tar.gz
Source1:        https://github.com/andrettin/wyrmsun/archive/v%{version}/%{name}-%{version}.tar.gz
Source3:        wyrmus.png
Patch0:         wyrmgus-fix-build.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  boost-devel
BuildRequires:  lua5.1-devel
#BuildRequires:  oaml-devel
#BuildRequires:  tolua++-devel
Requires:       %{name}-data >= %{version}-%{release}

%description
In the Wyrmsun universe a myriad of inhabited planets exist. Humans dwell
on Earth, while dwarves inhabit Nidavellir and elves nourish the world of
Alfheim. These peoples struggle to carve a place for themselves with their
tools of stone, bronze and iron. And perhaps one day they will meet one
another, beyond the stars...

%files
%doc Wyrmsun-%{version}/readme.txt
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{engine}
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%package data
Summary:        Data files for the Wyrmsun game
BuildArch:      noarch

%description data
This package contains arch-independent data files for the Wyrmsun game.

%files data
%{_gamesdatadir}/%{name}/

#----------------------------------------------------------------------

%prep
%setup -q -n Wyrmgus-%{version} -a1
%autopatch -p1

%build
%cmake -DWITH_BZIP2=ON \
       -DWITH_PHYSFS=ON \
       -DWITH_FLUIDSYNTH=ON \
       -DWITH_MNG=ON \
       -DENABLE_USEGAMEDIR=OFF
%cmake_build

%install
# Engine binary
install -D -m755 build/stratagus %{buildroot}%{_gamesbindir}/%{engine}

# Game data
pushd Wyrmsun-%{version}
install -d %{buildroot}%{_gamesdatadir}/%{name}
cp -a graphics maps music scripts sounds translations oaml.defs \
      %{buildroot}%{_gamesdatadir}/%{name}
install -D -m644 linux/wyrmsun.appdata.xml \
      %{buildroot}%{_metainfodir}/%{name}.appdata.xml
popd

# Launcher
install -d %{buildroot}%{_gamesbindir}
cat << EOF > %{buildroot}%{_gamesbindir}/%{name}
#!/bin/sh
%{engine} -d %{_gamesdatadir}/%{name} "\$@"
EOF
chmod +x %{buildroot}%{_gamesbindir}/%{name}

# Desktop entry
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Wyrmsun
GenericName=Strategy game
Comment=Real-time strategy game based on history, mythology and fiction
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

# Manpage
install -D -m644 doc/stratagus.6 \
        %{buildroot}%{_mandir}/man6/%{name}.6

# Icon
install -D -m644 %{_sourcedir}/%{name}-128.png \
        %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png
