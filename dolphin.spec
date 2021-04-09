Summary:	File manager for KDE focusing on usability
Name:		dolphin
Version:	21.03.90
Epoch:		1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		https://gitweb.frugalware.org/frugalware-current/raw/master/source/kde5/dolphin/allow-root.patch
Patch1:		dolphin-21.03.80-show-copyto-moveto-by-default.patch
URL:		https://www.kde.org/
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5BalooWidgets)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	cmake(packagekitqt5)
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	ruby
BuildRequires:	ninja
Recommends:	kio-fuse

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
%_datadir/qlogging-categories5/*.categories
%_bindir/dolphin
%_bindir/servicemenuinstaller
%_libdir/libkdeinit5_dolphin.so
%_qt5_plugindir/*.so
%_datadir/applications/org.kde.dolphin.desktop
%_datadir/config.kcfg/*.kcfg
%_datadir/knsrcfiles/servicemenu.knsrc
%_datadir/metainfo/org.kde.dolphin.appdata.xml
%_datadir/dbus-1/interfaces/org.freedesktop.FileManager1.xml
%_datadir/dbus-1/services/org.kde.dolphin.FileManager1.service
%_datadir/kglobalaccel/org.kde.dolphin.desktop
%_kde5_services/*.desktop
%_kde5_servicetypes/fileviewversioncontrolplugin.desktop
%_prefix/lib/systemd/user/plasma-dolphin.service
%_libdir/qt5/plugins/kf5/parts/dolphinpart.so
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/dolphin

#--------------------------------------------------------------------

%package handbook
Summary:	%{name} Handbook
BuildArch:	noarch

%description handbook
This package provides %{name} Handbook.

%files handbook -f handbook.list

#--------------------------------------------------------------------

%define dolphinprivate_major 5
%define libdolphinprivate %mklibname dolphinprivate %{dolphinprivate_major}

%package -n %{libdolphinprivate}
Summary:	Dolphin library
Group:		System/Libraries
Obsoletes:	%{mklibname dolphinprivate 15} < 15.12.0

%description -n %{libdolphinprivate}
Dolphin Library.

%files -n %{libdolphinprivate}
%_libdir/libdolphinprivate.so.%{dolphinprivate_major}*

#--------------------------------------------------------------------

%define dolphinvcs_major 5
%define libdolphinvcs %mklibname dolphinvcs %{dolphinvcs_major}

%package -n %{libdolphinvcs}
Summary:	Dolphin library
Group:		System/Libraries
Obsoletes:	%{mklibname dolphinvcs 15} < 15.12.0

%description -n %{libdolphinvcs}
Dolphin Library.

%files -n %{libdolphinvcs}
%_libdir/libdolphinvcs.so.%{dolphinvcs_major}*

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
%exclude %_libdir/libkdeinit5_dolphin.so
%_includedir/Dolphin
%_includedir/dolphin_export.h
%_includedir/dolphinvcs_export.h
%_libdir/cmake/DolphinVcs
%_libdir/*.so

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_kde5 -DSYSCONF_INSTALL_DIR="%{_sysconfdir}"
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
grep %_docdir %{name}.lang >handbook.list
grep -v %_docdir %{name}.lang >%{name}.translations
