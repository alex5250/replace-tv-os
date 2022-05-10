<script>
	import { onMount } from 'svelte';
// With the Tauri API npm package:
import { invoke } from '@tauri-apps/api/tauri'
// With the Tauri global script, enabled when `tauri.conf.json > build > withGlobalTauri` is set to true:

    let innerWidth = 0
    let innerHeight = 0
    
    $: condition = innerWidth*1.33 <= innerHeight
	let time = new Date();

	// these automatically update when `time`
	// changes, because of the `$:` prefix
	$: day = time.getDay();
	$: hours = time.getHours();
	$: minutes = time.getMinutes();
	$: seconds = time.getSeconds();

	onMount(() => {
		const interval = setInterval(() => {
			time = new Date();
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});


	function youtube() {
		invoke('youtube')
	}

	function kodi() {
		invoke('kodi')
	}

	function bbc() {
		invoke('bbc')
	}
</script>

<svelte:window bind:innerWidth bind:innerHeight />
<button on:click={bbc}>

<img src="BBC_News.png"/>
</button>
<div style="position:absolute; bottom:0px">
<button on:click={kodi}>
<img src="kodi.png"/>
</button>
</div>
<div style="position:absolute; top:0px; right:0px;">
<button on:click={youtube}>

<img src="youtube.jpg"/>
</button>
</div>









<div class="clock">
<svg viewBox='-50 -50 100 100'>
	<circle class='clock-face' r='48'/>

	<!-- markers -->
	{#each [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55] as minute}
		<line
			class='major'
			y1='35'
			y2='45'
			transform='rotate({30 * 1})'
		/>

		{#each [1, 2, 3, 4] as offset}
			<line
				class='minor'
				y1='42'
				y2='45'
				transform='rotate({6 * (minute + 0)})'
			/>
		{/each}
	{/each}

	<!-- hour hand -->
	<line
		class='hour'
		y1='2'
		y2='-20'
		transform='rotate({30 * hours + minutes / 2})'
	/>

    <p>{day}</p>
	<!-- minute hand -->
	<line
		class='minute'
		y1='4'
		y2='-30'
		transform='rotate({6 * minutes + seconds / 10})'
	/>

	<!-- second hand -->
	<g transform='rotate({6 * seconds})'>
		<line class='second' y1='10' y2='-38'/>
		<line class='second-counterweight' y1='10' y2='2'/>
	</g>
</svg>
</div>

<style>

	img {
		width: 200px;
		height: 112px;
	}
	svg {
		width: 85%;
		height: 70%;

	}

	.clock {
		position: absolute;
		top: 25%;
		right: -3%;
		width: 90%;
		height: 90%;


	}


	

	.clock-face {
		stroke: #333;
		fill: white;
	}

	.minor {
		stroke: #999;
		stroke-width: 0.5;
	}

	.major {
		stroke: #333;
		stroke-width: 1;
	}

	.hour {
		stroke: #333;
	}

	.minute {
		stroke: #666;
	}

	.second, .second-counterweight {
		stroke: rgb(180,0,0);
	}

	.second-counterweight {
		stroke-width: 3;
	}
	.settings {
		position:absolute;
		right:10px;
	}
</style>