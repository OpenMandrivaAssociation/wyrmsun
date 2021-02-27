%define oengine Wyrmgus
%define engine  wyrmgus
%define oname   Wyrmsun  

Name:           wyrmsun
Version:        4.1.4
Release:        1
Summary:        Real-time strategy game based on history, mythology and fiction
Group:          Games/Strategy
License:        GPLv2+ and CC-BY-SA
URL:            http://www.indiedb.com/games/wyrmsun
Source0:        https://github.com/andrettin/wyrmgus/archive/v%{version}/%{oengine}-%{version}.tar.gz
Source1:        https://github.com/andrettin/wyrmsun/archive/v%{version}/%{oname}-%{version}.tar.gz
Source3:        wyrmsun.png
#Patch0:         wyrmgus-fix-build.patch

BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  doxygen
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  %{_lib}qt5location-private-devel
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  boost-devel
#BuildRequires:  lua5.1-devel
BuildRequires:  lua-devel
BuildRequires:  pkgconfig(oaml)
BuildRequires:  tolua++-devel
Requires:       %{name}-data >= %{version}-%{release}

%description
In the Wyrmsun universe a myriad of inhabited planets exist. Humans dwell
on Earth, while dwarves inhabit Nidavellir and elves nourish the world of
Alfheim. These peoples struggle to carve a place for themselves with their
tools of stone, bronze and iron. And perhaps one day they will meet one
another, beyond the stars...

%files
%doc Wyrmsun-%{version}/readme.txt
#{_metainfodir}/%{name}.appdata.xml
#{_datadir}/applications/%{name}.desktop
#{_gamesbindir}/%{name}
%{_gamesbindir}/%{engine}
#{_iconsdir}/hicolor/128x128/apps/%{name}.png
#{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%package data
Summary:        Data files for the Wyrmsun game
BuildArch:      noarch

%description data
This package contains arch-independent data files for the Wyrmsun game.

%files data
#{_gamesdatadir}/%{name}/

#----------------------------------------------------------------------

%prep
%setup -q -n Wyrmgus-%{version} -a1
%autopatch -p1

%build
%cmake -DWITH_BZIP2=ON \
       -DWITH_PHYSFS=ON \
       -DWITH_FLUIDSYNTH=ON \
       -DWITH_MNG=ON \
       -DENABLE_USEGAMEDIR=OFF \
       -DCMAKE_BUILD_TYPE=Release \
       -DOpenGL_GL_PREFERENCE=GLVND
       
%make_build

%install
%make_install -C build

