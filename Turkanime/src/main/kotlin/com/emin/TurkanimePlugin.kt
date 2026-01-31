package com.emin
import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin
import android.content.Context

@CloudstreamPlugin
class TurkanimePlugin: Plugin() {
    override fun load(context: Context) {
        registerMainAPI(Turkanime())
    }
}
