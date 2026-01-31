package com.emin
import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin
import android.content.Context

@CloudstreamPlugin
class HdfilmizlePlugin: Plugin() {
    override fun load(context: Context) {
        registerMainAPI(Hdfilmizle())
    }
}
