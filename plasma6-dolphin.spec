%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20231104

Summary:	File manager for KDE focusing on usability
Name:		plasma6-dolphin
Version:	23.05.90
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/dolphin/-/archive/kf6/dolphin-kf6.tar.bz2#/dolphin-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Patch0:		https://gitweb.frugalware.org/frugalware-current/raw/master/source/kde5/dolphin/allow-root.patch
Patch1:		dolphin-21.03.80-show-copyto-moveto-by-default.patch
URL:		https://www.kde.org/
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Activities)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6MoreTools)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(KF6Baloo)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(packagekitqt6)
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	ruby
BuildRequires:	ninja
BuildRequires:	zsh
BuildRequires:	plasma6-xdg-desktop-portal-kde

%description
Dolphin is a file manager for KDE focusing on usability.
The main features of Dolphin are:
- Navigation bar for URLs, which allows to navigate quickly
     through the file hierarchy.
- View properties are remembered for each folder.
- Split of views is supported.
- Network transparency.
- Undo/redo functionality.
- Renaming of a variable number of selected items in one step.

Dolphin is not intended to be a competitor to Konqueror: Konqueror
acts as universal viewer being able to show HTML pages, text documents,
directories and a lot more, whereas Dolphin focuses on being only a file
manager. This approach allows to optimize the user interface for the task
of file management.

%files -f %{name}.translations
%{_qtdir}/plugins/dolphin
%{_qtdir}/plugins/kf6/parts/dolphinpart.so
%_datadir/qlogging-categories6/*.categories
%_bindir/dolphin
%_bindir/servicemenuinstaller
%_datadir/applications/org.kde.dolphin.desktop
%_datadir/config.kcfg/*.kcfg
%_datadir/knsrcfiles/servicemenu.knsrc
%_datadir/metainfo/org.kde.dolphin.appdata.xml
%_datadir/dbus-1/interfaces/org.freedesktop.FileManager1.xml
%_datadir/dbus-1/services/org.kde.dolphin.FileManager1.service
%_datadir/kglobalaccel/org.kde.dolphin.desktop
%_datadir/kconf_update/*
%{_datadir}/dolphin
%_prefix/lib/systemd/user/plasma-dolphin.service
%{_datadir}/zsh/site-functions/_dolphin
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/dolphin

#--------------------------------------------------------------------

%package handbook
Summary:	%{name} Handbook
BuildArch:	noarch

%description handbook
This package provides %{name} Handbook.

%files handbook -f handbook.list

#--------------------------------------------------------------------

%define dolphinprivate_major 6
%define libdolphinprivate %mklibname dolphinprivate %{dolphinprivate_major}

%package -n %{libdolphinprivate}
Summary:	Dolphin library
Group:		System/Libraries
Obsoletes:	%{mklibname dolphinprivate 15} < 15.12.0

%description -n %{libdolphinprivate}
Dolphin Library.

%files -n %{libdolphinprivate}
%_libdir/libdolphinprivate.so.%{dolphinprivate_major}*
%_libdir/libdolphinprivate.so.23*

#--------------------------------------------------------------------

%define dolphinvcs_major 6
%define libdolphinvcs %mklibname dolphinvcs %{dolphinvcs_major}

%package -n %{libdolphinvcs}
Summary:	Dolphin library
Group:		System/Libraries
Obsoletes:	%{mklibname dolphinvcs 15} < 15.12.0

%description -n %{libdolphinvcs}
Dolphin Library.

%files -n %{libdolphinvcs}
%_libdir/libdolphinvcs.so.%{dolphinvcs_major}*
%_libdir/libdolphinvcs.so.23*

#--------------------------------------------------------------------

%package devel
Summary:	Development stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	%{libdolphinprivate} = %{EVRD}
Requires:	%{libdolphinvcs} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname dolphin -d} < 15.08.2-2

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%_includedir/Dolphin
%_includedir/dolphin_export.h
%_includedir/dolphinvcs_export.h
%_libdir/cmake/DolphinVcs
%_libdir/*.so

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n dolphin-%{?git:kf6}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
grep %_docdir %{name}.lang >handbook.list
grep -v %_docdir %{name}.lang >%{name}.translations
