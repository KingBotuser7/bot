import { Context } from 'telegraf';
import { APIService } from '../services/api_service';

export class CommandHandlers {
    constructor(private apiService: APIService) {}

    async handleStart(ctx: Context) {
        await ctx.reply('👑 Welcome! I\'m King Bot - your GitHub repository analyzer.\n\nUse /help to see available commands.');
    }

    async handleHelp(ctx: Context) {
        await ctx.reply(
            '🔍 Available commands:\n\n' +
            '/check [repo-url] - Security check\n' +
            '/analyze [repo-url] - Code analysis\n' +
            '/contributors [repo-url] - Contributors info\n' +
            '/compare [repo1] [repo2] - Compare repos\n' +
            '/similarity [repo-url] - Code similarity check\n' +
            '/user [username] - User information'
        );
    }

    async handleAnalyze(ctx: Context) {
        await ctx.reply('🔒 This feature is currently under development.');
    }
}