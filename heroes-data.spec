Summary:	Game like Nibbles but different - datafiles
Summary(pl.UTF-8):	Gra w stylu Nibbles, ale inna - pliki z danymi
Name:		heroes-data
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
# Source0-md5:	015a95c16998bd0900f3a6cb6e6f26ac
URL:		http://heroes.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians".
This package containts data files.

%description -l pl.UTF-8
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeń i nowe własności. W tej grze musisz
manewrować małym pojazdem i zbierać dopalacze, unikając przeszkód i
śladów przeciwników, a nawet swojego własnego śladu. Są dostępne różne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjedź-pieszych".
Pakiet zawiera pliki z danymi.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/heroes/pics
%{_datadir}/heroes/levels
%{_datadir}/heroes/tilesets
