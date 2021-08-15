Name:           yle-dl
Version:        20210808
Release:        1%{?dist}
Summary:        Download videos from Yle servers
License:        GPLv3
URL:            https://github.com/aajanki/%{name}
Source0:        https://github.com/aajanki/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       ffmpeg >= 4.1
BuildArch:      noarch

%description
yle-dl is a tool for downloading media files from the video streaming services of the Finnish national broadcasting company Yle: Yle Areena, Elävä Arkisto and Yle news.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files
%doc ChangeLog README.md
%{_bindir}/%{name}
%{python3_sitelib}/yledl/
%{python3_sitelib}/yle_dl*.egg-info

%changelog
* Sun Aug 15 2021 Teemu Tervo <teemu.tervo iki.fi>
- Version bump
* Sun Jun 06 2021 Teemu Tervo <teemu.tervo iki.fi>
- Initial spec

