%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	File manager for KDE focusing on usability
Name:		dolphin
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/dolphin/-/archive/%{gitbranch}/dolphin-%{gitbranchd}.tar.bz2#/dolphin-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%(echo %{version} |cut -d. -f1-3)/src/dolphin-%{version}.tar.xz
%endif
URL:		https://www.kde.org/
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
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
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	ruby
BuildRequires:	ninja
BuildRequires:	zsh
BuildRequires:	plasma6-xdg-desktop-portal-kde
%rename plasma6-dolphin

%patchlist
https://gitweb.frugalware.org/frugalware-current/raw/%{gitbranchd}/source/kde5/dolphin/allow-root.patch
dolphin-21.03.80-show-copyto-moveto-by-default.patch
# Revert https://invent.kde.org/system/dolphin/-/commit/122fee5625f0285ec4ebda79162c72390989eb2a.patch
# It makes the UI less consistent for the sake of making it idiot friendly. This isn't GNOME.
revert-122fee5625f0285ec4ebda79162c72390989eb2a.patch

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
%{_libdir}/kconf_update_bin/dolphin_25.04_update_statusandlocationbarssettings
%{_datadir}/dolphin
%{_prefix}/lib/systemd/user/plasma-dolphin.service
%{_datadir}/zsh/site-functions/_dolphin
%{_datadir}/icons/hicolor/scalable/apps/org.kde.dolphin.svg
%dir %{_qtdir}/plugins/kf6/kfileitemaction
%{_qtdir}/plugins/kf6/kfileitemaction/movetonewfolderitemaction.so
%{_datadir}/polkit-1/actions/org.kde.dolphin.policy

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
%_libdir/libdolphinprivate.so.25*

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
%_libdir/libdolphinvcs.so.25*

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

%install -a
grep %_docdir %{name}.lang >handbook.list
grep -v %_docdir %{name}.lang >%{name}.translations

mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
cat >%{buildroot}%{_datadir}/polkit-1/actions/org.kde.dolphin.policy <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-FileCopyrightText: no
     SPDX-License-Identifier: CC0-1.0
-->
<!DOCTYPE policyconfig PUBLIC
"-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
"http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>

 <vendor>Dolphin</vendor>
 <vendor_url>https://apps.kde.org/dolphin</vendor_url>

 <action id="org.kde.dolphin.pkexec.run">
    <description>Dolphin file manager</description>
    <message>Authentication is required to run the Dolphin file manager in admin mode</message>
    <icon_name>org.kde.dolphin</icon_name>
    <defaults>
     <allow_any>no</allow_any>
     <allow_inactive>no</allow_inactive>
     <allow_active>auth_admin</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">%{_bindir}/dolphin</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
 </action>
</policyconfig>
EOF
