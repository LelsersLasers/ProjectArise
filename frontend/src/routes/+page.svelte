<script>
    import { onMount } from 'svelte';
    import BulletList from '$lib/BulletList.svelte';

    const FLASK_URL = 'https://projectarise.pythonanywhere.com/';
    // const FLASK_URL = 'http://64.98.192.13:3001/';
    // const FLASK_URL = 'http://localhost:3001/';

    let title = 'Project ARISE';

    let overlay = false;
    let remove_info = {};


    let fileInput;
    let img;


    let results = null;

    let temp_results = [...Array(5).keys()]
        .map(_ => {
            return {
                'label': 'Loading...',
                'confidence_display': 0.0,
            }
        })

    let loading = false;
    let loading_text = 'LOADING...';
    let loading_text_animation = 3;
    setInterval(() => {
        loading_text_animation = (loading_text_animation + 1) % 4;
        loading_text = 'LOADING' + '.'.repeat(loading_text_animation);
    }, 120);


    // Placeholder image; less work to just make it base64 like this than use static files
    let input_b64 = 'data:image/png;base64,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';
    let image_b64 = '';
    function upload() {
        if (document.getElementById('file').files.length == 0) {
            return;
        }

        const file = document.getElementById('file').files[0];
        const reader = new FileReader();
        reader.onload = function() {
            input_b64 = reader.result;
            image_b64 = input_b64.split(',')[1];
            go();
        }
        reader.readAsDataURL(file);
    }

    function go() {
        loading = true;

        const url = FLASK_URL + 'classify';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'image_b64': image_b64,
            }),
        })
            .then(response => response.json())
            .then(data => {
                results = data;
                for (let i = 0; i < results.length; i++) {
                    results[i]['confidence_display'] = (results[i]['confidence'] * 100).toFixed(0);
                }
                
                console.log(results);
                loading = false;
            })
            .catch(error => {
                console.error('Error:', error);
                loading = false;
            });
    }

    function imageClick() {
        fileInput.click();
    }

    function resultClick(i) {
        remove_info = results[i]['info'];
        overlay = true;
    }

    function back() {
        overlay = false;
    }
</script>

<style>
    #underlay {
        padding: 0;
        margin: 0;
        width: 100%;
        height: 100%;

        background-color: var(--bgYellow);

        padding-top: 24px;

        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    #underlay img {
        display: block;
        
        width: 100%;
        max-width: 300px;

        max-height: 300px;

        /* margin-top: 24px; */
        /* margin-bottom: 24px; */
        margin-left: auto;
        margin-right: auto;

        border-radius: 50px;
        border: 12px solid var(--darkGreen);
    }

    #underlay .info {
        text-align: center;
    }


    #underlay #results {
        width: 100%;
        max-width: 325px;

        margin: 0 auto;
        margin-bottom: 20px;
    }
    #underlay .result {
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 12px;
        padding-right: 16px;

        margin: 8px;


        background-color: var(--darkGreen);
        color: white;
        border-radius: 20px;
    }
    #underlay .live {
        cursor: pointer;
    }
    #underlay .resultBase {
        display: inline-block;
        margin: 0;
        padding: 0;
    }
    #underlay .resultConfidence {
        font-weight: bold;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    #underlay .resultLabel {
        text-transform: capitalize;
        font-style: italic;
    }
    #underlay .resultArrow {
        float: right;
    }

    @media (min-width: 768px) {
        #underlay img {
            width: 100%;
            max-width: 375px;

            max-height: 375px;
        }
        #underlay #results {
            max-width: 400px;
        }
    }

    #underlay .none {
        display: none;
    }


    #overlay {
        position: fixed;
        width: 100vw;
        height: 100%;
        background-color: var(--bgGreen);
        z-index: 2;
        overflow-y: auto;
        overflow-x: hidden;
    }

    #overlay hr {
        width: 90%;
        margin: 0 auto;
        margin-top: 20px;
        margin-bottom: 20px;
        border-color: white;
    }
    @media (min-width: 768px) {
        #overlay hr {
            width: 55%;
        }
    }

    #overlay h1 {
        text-align: center;
        text-transform: capitalize;
        margin-top: 20px;
        margin-bottom: 0px;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }

    #overlay #scientificName {
        text-align: center;
        text-transform: capitalize;
        font-style: italic;
        margin-bottom: 0px;
        margin-top: 10px;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;

    }

    #overlay .sectionHeader {
        text-align: center;
        text-decoration: underline;
        margin-bottom: 10px;
    }

    #overlay #description {
        margin-top: 0px;
    }


    #overlay .stickyFooter {
        position: fixed;
        left: 0;
        bottom: 0;
        background: var(--bgGreen);
        color: white;
        /* width: 97vw; */
        width: 100%;

        /* margin-bottom: 2vw; */
        margin-top: 3vw;
        /* margin-left: 1.5vw; */
        /* margin-right: 1.5vw; */
        /* border-radius: 20px; */

        padding-top: 8px;
        padding-bottom: 8px;

        display: flex;
        justify-content: center;
        align-items: center;
        
        cursor: pointer;
    }
    #backButton {
        width: 95%;
        max-width: 300px;

        display: flex;
        justify-content: center;
        align-items: center;

        background-color: var(--darkGreen);
        color: white;
        border-radius: 20px;
        padding: 10px;
    }
</style>


<svelte:head>
    <title>{title}</title>
</svelte:head>



{#if overlay}
    <div id="overlay">
        <h1>{remove_info["commonName"]}</h1>
        <p id="scientificName">{remove_info["scientificName"]}</p>


        <hr />

        <h3 id="description" class="sectionHeader">Description</h3>
        <BulletList content={remove_info["description"]} />

        <h3 class="sectionHeader">Hazards/Protective Equipment</h3>
        <BulletList content={remove_info["suggestions"]} />

        <h3 class="sectionHeader">Manual Removal</h3>
        <BulletList content={remove_info["manualRemoval"]} />

        {#if remove_info["chemicalRemoval"].length > 0}
            <h3 class="sectionHeader">Chemical Removal</h3>
            <BulletList content={remove_info["chemicalRemoval"]} />
        {/if}

        <h3 class="sectionHeader">Other Information</h3>
        <BulletList content={remove_info["otherInfo"]} />

        <br />
        <br />
        <br />


        <div class="stickyFooter">
            <div id="backButton" on:click={back}>
                Back
            </div>
        </div>
    </div>
{:else}
    <div id="underlay">
        <input class="none" type="file" id="file" name="file" accept="image/*" on:input={upload} bind:this={fileInput} />

        <img src={input_b64} on:click={imageClick} bind:this={img} />

        {#if loading}
            <p class="info">{loading_text}</p>
            <div id="results">
                {#each temp_results as temp_result}
                    <div class="result">
                        <p class="resultBase resultConfidence">{temp_result["confidence_display"]}%</p>
                        <p class="resultBase resultLabel">{temp_result["label"]}</p>
                        <p class="resultBase resultArrow">&#9203;</p>
                    </div>
                {/each}
            </div>
        {:else if results == null}
            <p class="info">Click icon to take or upload a photo</p>
        {:else}
            <p class="info">Tap on an item to view removal instructions</p>
            <div id="results">
                {#each results as result, i}
                    <div class="result live" on:click={() => resultClick(i)}>
                        <p class="resultBase resultConfidence">{result["confidence_display"]}%</p>
                        <p class="resultBase resultLabel">{result["label"]}</p>
                        <p class="resultBase resultArrow">&rsaquo;</p>
                    </div>
                {/each}
            </div>
        {/if}
    </div>
{/if}