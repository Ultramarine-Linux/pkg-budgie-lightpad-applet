%undefine       _disable_source_fetch
Name:           budgie-lightpad-applet
Version:        0.0.2
Release:        1%{?dist}
Summary:        Lightweight and stylish fullscreen application launcher.

License:        GPLv3
URL:            https://github.com/UbuntuBudgie/budgie-lightpad-applet
Source0:        https://github.com/UbuntuBudgie/budgie-lightpad-applet/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gtk3-devel
BuildRequires:  budgie-desktop-devel
BuildRequires:  libpeas-devel
BuildRequires:  meson
BuildRequires:  vala
Requires:       budgie-desktop
Requires:       budgie-extras
Requires:       lightpad

%description
%{summary}

%prep
%autosetup


%build
%meson
%meson_build


%install
rm -rf $RPM_BUILD_ROOT
%meson_install


%files
%license LICENSE
%{_libdir}/budgie-desktop/plugins/lightpad/Lightpad.plugin
%{_libdir}/budgie-desktop/plugins/lightpad/liblightpad.so
%changelog
* Mon Jan 31 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
