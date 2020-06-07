"""

Main entry point

"""
import requests, re
from lxml import html


def get_characters_urls_from_profile(profile_url: str):
    characters_urls = []

    page = requests.get(profile_url)
    tree = html.fromstring(page.content)

    _test = '//*[@class="hero-tabs MediaCarousel-scroll"]'
    chars = tree.xpath(_test)
    if chars:
        for char in chars[0].xpath('li'):
            profile_nr = char.xpath('a[1]')
            if profile_nr:
                char_code = profile_nr[0].attrib['href']
                char_name = False
                for x in profile_nr[0].xpath('span[@class="name"]'):
                    char_name = x.text_content().strip()

            characters_urls.append('{}/hero/{}'.format(profile_url, char_code))
                # result = re.search(r'<div class="detail-text">((.*\s*)*?)<span class="clear">', text)


    return characters_urls


if __name__ == '__main__':

    for x in get_characters_urls_from_profile(r'https://eu.diablo3.com/en/profile/Ralicx-2273/'):
        print(x)

'''
<ul class="hero-tabs MediaCarousel-scroll" style="width: 1746px;">


						<li class="MediaCarousel-thumb">
							<a class="hero-tab barbarian-female active" href="133589041" data-tooltip="#hero-tab-tooltip-0">
								<span class="hero-portrait">
										<span class="small-seasonal-leaf"></span>
								</span>
								<span class="level">70</span>
								<span class="name">Burla</span>
							</a>



	<div id="hero-tab-tooltip-0" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">Burla</h2>

			<p>
				<strong>70</strong> female
				 - <span class="d3-color-seasonal">Seasonal Hero</span>
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab crusader-male " href="134261017" data-tooltip="#hero-tab-tooltip-1">
								<span class="hero-portrait">
										<span class="small-seasonal-leaf"></span>
								</span>
								<span class="level">70</span>
								<span class="name">Charlemagne</span>
							</a>



	<div id="hero-tab-tooltip-1" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">Charlemagne</h2>

			<p>
				<strong>70</strong> male
				 - <span class="d3-color-seasonal">Seasonal Hero</span>
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab necromancer-male " href="124935330" data-tooltip="#hero-tab-tooltip-2">
								<span class="hero-portrait">
								</span>
								<span class="level">70</span>
								<span class="name">Emomuel</span>
							</a>



	<div id="hero-tab-tooltip-2" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">Emomuel</h2>

			<p>
				<strong>70</strong> male
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab monk-female " href="127544319" data-tooltip="#hero-tab-tooltip-3">
								<span class="hero-portrait">
								</span>
								<span class="level">70</span>
								<span class="name">HITME</span>
							</a>



	<div id="hero-tab-tooltip-3" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">HITME</h2>

			<p>
				<strong>70</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab witch-doctor-female " href="127350103" data-tooltip="#hero-tab-tooltip-4">
								<span class="hero-portrait">
								</span>
								<span class="level">70</span>
								<span class="name">TaiDalma</span>
							</a>



	<div id="hero-tab-tooltip-4" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">TaiDalma</h2>

			<p>
				<strong>70</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab necromancer-male " href="131034385" data-tooltip="#hero-tab-tooltip-5">
								<span class="hero-portrait">
										<span class="small-seasonal-leaf"></span>
								</span>
								<span class="level">70</span>
								<span class="name">Vlad</span>
							</a>



	<div id="hero-tab-tooltip-5" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">Vlad</h2>

			<p>
				<strong>70</strong> male
				 - <span class="d3-color-seasonal">Seasonal Hero</span>
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab wizard-female " href="124631594" data-tooltip="#hero-tab-tooltip-6">
								<span class="hero-portrait">
								</span>
								<span class="level">70</span>
								<span class="name">hermione</span>
							</a>



	<div id="hero-tab-tooltip-6" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">hermione</h2>

			<p>
				<strong>70</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab barbarian-female " href="123210710" data-tooltip="#hero-tab-tooltip-7">
								<span class="hero-portrait">
								</span>
								<span class="level">64</span>
								<span class="name">BattleWench</span>
							</a>



	<div id="hero-tab-tooltip-7" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">BattleWench</h2>

			<p>
				<strong>64</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab monk-female " href="123552406" data-tooltip="#hero-tab-tooltip-8">
								<span class="hero-portrait">
								</span>
								<span class="level">54</span>
								<span class="name">FistyCuffs</span>
							</a>



	<div id="hero-tab-tooltip-8" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">FistyCuffs</h2>

			<p>
				<strong>54</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab necromancer-female " href="124900492" data-tooltip="#hero-tab-tooltip-9">
								<span class="hero-portrait">
								</span>
								<span class="level">26</span>
								<span class="name">Morticia</span>
							</a>



	<div id="hero-tab-tooltip-9" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">Morticia</h2>

			<p>
				<strong>26</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab necromancer-female " href="129307511" data-tooltip="#hero-tab-tooltip-10">
								<span class="hero-portrait">
								</span>
								<span class="level">22</span>
								<span class="name">Morta</span>
							</a>



	<div id="hero-tab-tooltip-10" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">Morta</h2>

			<p>
				<strong>22</strong> female
			</p>
		</div>
	</div>
						</li>


						<li class="MediaCarousel-thumb">
							<a class="hero-tab witch-doctor-male " href="124350001" data-tooltip="#hero-tab-tooltip-11">
								<span class="hero-portrait">
								</span>
								<span class="level">1</span>
								<span class="name">shakers</span>
							</a>



	<div id="hero-tab-tooltip-11" style="display:none">
		<div class="hero-tab-tooltip profile-tooltip">
			


	<h2 class="subheader-2">shakers</h2>

			<p>
				<strong>1</strong> male
			</p>
		</div>
	</div>
						</li>
							<li class="MediaCarousel-thumb">
								<span class="hero-tab empty-hero"></span>
							</li>
							<li class="MediaCarousel-thumb">
								<span class="hero-tab empty-hero"></span>
							</li>
							<li class="MediaCarousel-thumb">
								<span class="hero-tab empty-hero"></span>
							</li>
							<li class="MediaCarousel-thumb">
								<span class="hero-tab empty-hero"></span>
							</li>
							<li class="MediaCarousel-thumb">
								<span class="hero-tab empty-hero"></span>
							</li>
							<li class="MediaCarousel-thumb">
								<span class="hero-tab empty-hero"></span>
							</li>
				</ul>
'''