%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	File manager for KDE focusing on usability
Name:		plasma6-dolphin
Version:	24.02.0
Release:	%{?git:0.%{git}.}3
License:	GPLv2+
Group:		Graphical desktop/KDE
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/dolphin/-/archive/%{gitbranch}/dolphin-%{gitbranchd}.tar.bz2#/dolphin-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/dolphin-%{version}.tar.xz
%endif
Patch0:		https://gitweb.frugalware.org/frugalware-current/raw/%{gitbranchd}/source/kde5/dolphin/allow-root.patch
Patch1:		dolphin-21.03.80-show-copyto-moveto-by-default.patch
# https://bugs.kde.org/show_bug.cgi?id=481952
Patch2:		https://invent.kde.org/system/dolphin/-/commit/4dc9510a2a8ceb35503cc7e81c2024774491ce8a.patch
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
BuildRequires:	cmake(PlasmaActivities)
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
BuildRequires:	cmake(KF6BalooWidgets)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(packagekitqt6)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets
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
%{_prefix}/lib/systemd/user/plasma-dolphin.service
%{_datadir}/zsh/site-functions/_dolphin
%{_datadir}/icons/hicolor/scalable/apps/org.kde.dolphin.svg

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
%_libdir/libdolphinprivate.so.24*

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
%_libdir/libdolphinvcs.so.24*

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
%autosetup -p1 -n dolphin-%{?git:%{gitbranchd}}%{!?git:%{version}}
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
